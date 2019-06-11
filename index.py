import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from app import server
from app import app

from layouts import leak_product, fail
# There will be more as I add more pages

# import callbacks
# I will write callbacks.py later.

app.index_string = '''
<!DOCTYPE html>
<html>
    <head>
        {%metas%}
        <title> ABDC Drug Leakage Report </title>
        {%css%}
    </head>
    <body>
        {%app_entry%}
        <footer>
            {%config%}
            {%scripts%}
            {%renderer%}
        </footer>
        <div>ABDC Drug Leakage Report</div>
    </body>
</html>
'''


app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])


# Update the page depending on the URL
# # # # # # # # #
@app.callback(Output('page-content', 'children'),[Input('url', 'pathname')])

def display_page(pathname):
    if pathname == '/leak_product/':
        return leak_product
    else:
        return fail

###################

external_css = ["https://cdnjs.cloudflare.com/ajax/libs/normalize/7.0.0/normalize.min.css",
                "https://cdnjs.cloudflare.com/ajax/libs/skeleton/2.0.4/skeleton.min.css",
                "//fonts.googleapis.com/css?family=Raleway:400,300,600",
                "https://fonts.googleapis.com/css?family=Poppins:500&display=swap"
                "https://maxcdn.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css",
                "https://codepen.io/dmcomfort/pen/JzdzEZ.css"]

for css in external_css:
    app.css.append_css({"external_url": css})

# external_js = ["https://code.jquery.com/jquery-3.2.1.min.js",
#                "https://codepen.io/bcd/pen/YaXojL.js"]

# for js in external_js:
#     app.scripts.append_script({"external_url": js})

if __name__ == '__main__':
    app.run_server(debug=True)
