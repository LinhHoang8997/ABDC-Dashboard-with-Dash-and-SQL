import dash_core_components as dcc
import dash_html_components as html
# import dash_table
# from components import Header, print_button
from datetime import datetime as dt
from datetime import date, timedelta
import pandas as pd


# Read from SQL
# data = pd.DataFrame()

home  =  html.Div(children=[
    html.H1(children='HOME PAGE'),

    html.H2(children='''
        My first web dashboard
    '''),

    dcc.Graph(
        id='example-graph',
        figure={
            'data': [
                {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'},
                {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': u'Montréal'},
            ],
            'layout': {
                'title': 'Placeholder chart from Plotly'
            }
        }
    )
])


fail  =  html.Div(children=[
    html.H1(children='NO PAGE HERE.')
])
