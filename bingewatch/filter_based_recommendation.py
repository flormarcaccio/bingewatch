"""
This module contains the layout for the second tab of the visualization.
It is being called by main.py.
"""
import dash_html_components as html
import dash_core_components as dcc
from bingewatch.app import IMDB_DF
from bingewatch.app import GENRES


EXTERNAL_STYLESHEETS = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

TAB2_LAYOUT = html.Div([
    html.Div([
        html.Label('Filter by:'),
        dcc.Checklist(
            id='filter-checklist',
            options=[
                {'label': 'Genre', 'value': 'Genre'},
                {'label': 'Year', 'value': 'Year'}],
            value=['Genre', 'Year'])],
             style={'margin-bottom': '50px', 'margin-left':'20px'}),
    html.Div(id='slider-wrapper', children=[
        html.Label('Year:'),
        dcc.Slider(
            id='year-slider',
            min=int(IMDB_DF['startYear'].min()),
            max=int(IMDB_DF['startYear'].max()),
            value=int(IMDB_DF['startYear'].max()),
            included=False,
            updatemode='drag',
            tooltip={'always_visible': True})],
             style={'margin-bottom': '50px',
                    'margin-left': '20px',
                    'margin-right': '20px',
                    'text-orientation': 'mixed'}),
    html.Div([
        html.Div([
            html.Label('Select the genre you would like to see:'),
            dcc.Dropdown(
                id='genre-dropdown',
                options=[{'label': i, 'value': i} for i in GENRES],
                placeholder='Select Genre',)],
                 style={'width': '48%',
                        'margin-bottom': '50px',
                        'margin-left':'20px',
                        'display': 'inline-block'}),
        html.Div([
            html.Label('Select the type of content you would like to see:'),
            dcc.RadioItems(
                id='title-type',
                options=[{'label': 'Movie', 'value' : 'movie'},
                         {'label' :'TV Series', 'value': 'tvSeries'}],
                value='movie',
                labelStyle={'display': 'inline-block', 'padding': '10px'})],
                 style={'width': '48%', 'float': 'right', 'display': 'inline-block'}),
        ]),

    html.Div([
        dcc.Graph(style={'height': '400px',
                         'width': '1300px',
                         'margin-left':'auto',
                         'margin-right':'auto'},
                  id='graph-with-slider')])
    ])
