import dash
import dash_core_components as dcc
import dash_html_components as html

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

# app = dash.Dash(__name__, external_stylesheets=external_stylesheets, url_base_pathname='/index/')
app = dash.Dash(__name__, external_stylesheets=external_stylesheets, url_base_pathname='/home/')
server = app.server
app.config.suppress_callback_exceptions = True

