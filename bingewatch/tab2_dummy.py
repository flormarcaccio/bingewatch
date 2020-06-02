import dash
import dash_html_components as html
import dash_core_components as dcc
import plotly.graph_objects as go
import pandas as pd
from dash.dependencies import Input, Output
import numpy as np
import pickle
import dash_table
# from dash_dashboards_files.helper_functions import userchoice_based_movie_recommendation
import netflix as nmr

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

movies_df = nmr.reading_movie_title_csv()

colors = {
    'background': 'white',
    'background1': 'light blue',
    'text': 'black'
}

# noinspection PyPackageRequirements,PyPackageRequirements,PyPackageRequirements
tab2_layout = html.Div(style={'backgroundColor': colors['background']}, children=[
    html.Div(className='div-user-controls',
             children=[
                 html.Div(
                     className='div-for-dropdown-and-table',
                     children=[
                         dcc.Dropdown(id='movie_list_input2', options=nmr.get_options(movies_df['Display'].unique()),
                                      value=[movies_df['Display'].iloc[206]], searchable=True
                                      )
                     ]
                 )
             ]
             ),
    html.Div(id='output',
             className='row',
             children=[html.Div(id='my-table2',
                                className='six columns')
                       ]
             )

]
)


