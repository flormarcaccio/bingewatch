import dash
from dash.dependencies import Input, Output
import dash_html_components as html
import dash_core_components as dcc
import tab2
import movie_recommendation_view1_v1

app = dash.Dash()

app.config['suppress_callback_exceptions'] = True

app.layout = html.Div([
    html.H1('Dash Tabs component demo'),
    dcc.Tabs(id="tabs-example", value='tab-1-example', children=[
        dcc.Tab(label='Tab One', value='tab-1-example'),
        dcc.Tab(label='Tab Two', value='tab-2-example'),
    ]),
    html.Div(id='tabs-content-example')
])

@app.callback(Output('tabs-content-example', 'children'),
              [Input('tabs-example', 'value')])

def render_content(tab):
    if tab == 'tab-1-example':
        #return movie_recommendation_view1_v1.tab_1_layout
        return 0
    elif tab == 'tab-2-example':
        return tab2.layout
