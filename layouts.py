import dash_core_components as dcc
import dash_html_components as html
# from datetime import datetime as dt
# from datetime import date, timedelta
import plotly.graph_objs as go
import pandas as pd
import numpy as np


# Read from SQL by calling functions defined in /model/
# data = pd.DataFrame()

################ HOME - Leakage by Product ########################
# Data Logic
from model.product_sales_db import get_product_sales
data_mfg_sum = get_product_sales("mfg_sum")

data_bub_compo = get_product_sales("bub_compo")
mfg_labels = data_bub_compo.sort_values(by="rank")["mfg_nam"].drop_duplicates()


### Drawing the first scene
leak_product  =  html.Div([
    html.H1(children='ABDC Leakage Report'),

    # First Set of charts
    html.H2(children='''
        Leakage by Product and Manufacturer
    '''),

    html.H3(children='''
        Top 10 Manufacturers that account for most leakage
    '''),
    dcc.Graph(
        id='leakage-top10-mfg',
        figure={
            'data': [go.Bar(x=data_mfg_sum.mfg_nam,
                            y=data_mfg_sum.total_leak_26w,
                            marker=dict(color='#be2429'),
                            )
                    ],
            'layout': go.Layout(
                yaxis={'title': 'Sales lost to leakage'},
                margin={'t': 20,'b':120}
            ),

        }
    ),

    html.H3(children='''
        Products within the above manufacturers and their leakage
    '''),

    dcc.Graph(
        id='leakage-mfg-composition',
        figure={
            'data': [go.Scatter(
                        x=data_bub_compo['rank'],
                        y=data_bub_compo['avg_leak_26'],
                        mode='markers',
                        text=data_bub_compo['ndc_desc'],
                        hovertemplate = '%{text} - Leak rate: %{y:.2f}',
                        marker=dict(
                            color=data_bub_compo['total_leak_26w'],
                            size=np.log(data_bub_compo['total_leak_26w'])*3,
                            opacity=0.8,
                            showscale=True
                        )
                    )],
            'layout': go.Layout(
                yaxis={'title': 'Leakage Rate over 26 weeks'},
                xaxis=dict(
                    tickvals= np.arange(1,11),
                    ticktext=mfg_labels
                ),
                margin={'t': 20,'b':120}
                # legend={'x': 0, 'y': 1},
                # hovermode='closest'
            )
        }
    )

])

######### PRODUCT INFORMATION #############






######### NO PAGE AT ALL #############
fail  =  html.Div(children=[
    html.H1(children='NO PAGE HERE.')
])
