
import psycopg2
import sqlalchemy as db
from sqlalchemy.sql import text
import pandas as pd

engine = db.create_engine('postgresql+psycopg2://postgres:__pass_hidden__@localhost:5433/' + 'abdc_drug_db', client_encoding='utf8')

def get_product_sales(subject):
    connection = engine.connect()

    filter_add_on = ""
    statement = text('SELECT * FROM '
    '(SELECT '
        's.ndc,'
        'SUM(s.purch_qty_13w) as total_pur_qt_13,'
        'SUM(s.dspn_qty_13w) as total_dspn_qt_13,'
        'AVG(leak_rate_13w) as avg_leak_13,'
        'SUM(purch_qty_26w) as total_pur_qt_26,'
        'SUM(dspn_qty_26w) as total_dspn_qt_26,'
        'SUM(leak_dol_13w) as total_leak_13w,'
        'SUM(leak_dol_26w) as total_leak_26w,'
        'AVG(leak_rate_26w) as avg_leak_26,'
        'AVG(cogs_prc_mtrc) as avg_cogs '
        ' FROM sales_record AS s '
        'GROUP BY s.ndc'
    ') AS t '
    'LEFT JOIN product as pr '
    'ON t.ndc = pr.ndc' + filter_add_on)
    result = connection.execute(statement).fetchall()
    df = pd.DataFrame(result, columns = result[0].keys())
    df = df.loc[:,~df.columns.duplicated()]
    connection.close()

    # Process data for use in the top 10 barchart
    data_mfg_sum = df.groupby("mfg_nam").sum().drop([col for col in df.columns if "avg" in col], axis=1).reset_index()
    data_mfg_sum = data_mfg_sum.sort_values(by="total_leak_26w", ascending=False).head(10)
    if (subject == "mfg_sum"):
        return data_mfg_sum

    # Process data for use in the composition bubble chart
    key_order = data_mfg_sum.reset_index().reset_index()[['level_0','mfg_nam']]
    mean_df = df[['ndc','avg_leak_26']].groupby("ndc").mean().reset_index()
    sum_df = df[['ndc','total_leak_26w']].groupby("ndc").sum().reset_index()
    mfg_nam_df = df[['ndc','mfg_nam']].drop_duplicates()
    ndc_desc_df = df[['ndc','ndc_desc']].drop_duplicates()
    combi = pd.merge(mean_df,sum_df,on="ndc",how="left")
    combi = pd.merge(combi,ndc_desc_df,on="ndc",how="left")
    combi = pd.merge(combi,mfg_nam_df,on="ndc",how="left")
    combi = pd.merge(combi,key_order,on="mfg_nam",how="left")
    data_bub_compo = combi.dropna()
    data_bub_compo = data_bub_compo.rename(columns={'level_0': 'rank'})
    data_bub_compo = data_bub_compo.reset_index()
    data_bub_compo['rank'] = data_bub_compo['rank']+1
        # make 1, rather than 0 the starting point in the chart

    data_bub_compo = data_bub_compo[data_bub_compo.total_leak_26w>=0]
    data_bub_compo = data_bub_compo[data_bub_compo.avg_leak_26>=0]
       # negative values (overbuying) are irrelevant to leakage
    if (subject == "bub_compo"):
        return data_bub_compo
