import dash
import dash_html_components as html
import dash_core_components as dcc
import plotly.graph_objects as go
import pandas as pd
from dash.dependencies import Input, Output
import numpy as np
import pickle
import dash_table
#from dash_dashboards_files.helper_functions import userchoice_based_movie_recommendation
from helper_functions import *

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

## Reading movie_title.csv for movie list dropdown
movie_list = pd.read_csv("../data/movie_titles.csv", sep=",")
movie_list.sort_values(by='Final_title', ascending=True, inplace=True)

##Creating dummy file for debugging purpose
##df_final11 = movie_list[:10]

# Initialize the app
app = dash.Dash(__name__)
app.config.suppress_callback_exceptions = True

colors = {
    'background': '#665544',
    'background1': '#112233',
    'text': '#7FBDFF'
}


## Setting up function for our dropdowns: movie_list, year_list, genre list
def get_options(movie_list):
    """
    List all the unique elements of a column in dropdown
    Args:
        movie_list: Final_title
    Returns: list of columns
    """
    dict_list = []
    for i in movie_list:
        dict_list.append({'label': i, 'value': i})
    print(type(dict_list))
    dict_list.pop()
    return dict_list


app.layout = html.Div(style={'backgroundColor': colors['background']}, children=[
    html.H1(
        children='Movie Recommendation: Get your next watch here!',
        style={
            'textAlign': 'center',
            'color': colors['text']
        }
    ),
    html.Div(children='This is a movie recommendation webpage. Get your next watch just by entering either your '
                      'favorite movie. You are also free to enter your most liked genre or year of watch and we will '
                      'find the most relevant movies and/or tv series that will absolutely delight you! So, lets go!!',
             style={
                 'textAlign': 'center',
                 'color': colors['text']
             }
             ),
    html.Div(className='div-user-controls',
             children=[
                 html.H4(children='Enter a movie you have loved watching: ',
                         style={
                             'textAlign': 'left',
                             'color': colors['text']
                         }),
                 html.Div(
                     className='div-for-dropdown-and-table',
                     children=[
                         dcc.Dropdown(id='movie_list_input', options=get_options(movie_list['Display'].unique()),
                                      value=[movie_list['Display'].iloc[3]],
                                      style={'background': colors['background']},
                                      searchable=True
                                      )
                     ],
                     style={
                         'textAlign': 'left',
                         'color': colors['text']
                     }
                 )

             ]
             ),
    html.Div(id='my-table')
]
)


def generate_table(dataframe, max_rows=10):
    return html.Table([
        html.Thead(
            html.Tr([html.Th(col) for col in dataframe.columns])
        ),
        html.Tbody([
            html.Tr([
                html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
            ]) for i in range(min(len(dataframe), max_rows))
        ])
    ])


@app.callback(Output('my-table', 'children'), [Input('movie_list_input', 'value')])
def update_figure(selected_movie):
    movie_list = userchoice_based_movie_recommendation(selected_movie)
    movie_list_op = movie_list
    return generate_table(movie_list_op)


if __name__ == '__main__':
    app.run_server(debug=True)

"""

html.Div(id ='output',
             children=[
                 html.P('We believe based on your liking for the above movie, the following 10 movies will interest you the most:',
                        style={
                            'textAlign': 'center',
                            'color': colors['text']
                            }
                        )
                 ]
             ),
    dash_table.DataTable(id='df_output',
                         columns=[{"name": i, "id": i} for i in movielist.columns]
                         )

"""
