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
tab1 = dash.Dash(__name__, external_stylesheets=external_stylesheets)

## Reading movie_title.csv for movie list dropdown
movies_df = nmr.reading_movie_title_csv()

# Initialize the app
tab1 = dash.Dash(__name__, external_stylesheets=external_stylesheets)
tab1.config.suppress_callback_exceptions = True

colors = {
    'background': 'white',
    'background1': 'light blue',
    'text': 'black'
}

tab1.layout = html.Div(style={'backgroundColor': colors['background']}, children=[
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
                         dcc.Dropdown(id='movie_list_input', options=nmr.get_options(movies_df['Display'].unique()),
                                      value=[movies_df['Display'].iloc[206]], searchable=True
                                      )
                     ]
                 ),
                 html.Div(children=[html.H1("\n \n")]),
                 html.Div(id='after_input_text',
                          children=[html.P("\n\nWe believe based on your liking for the above movie, "
                                           "the following 10 movies will interest you the most:")],
                          style={'text-orientation': 'left'}
                          )
             ]
             ),
    html.Div(id='my-table',
             style={'width': '100%',
                    'margin-top': '15px',
                    'margin-bottom': '50px',
                    'margin-left': '80px',
                    'display': 'inline-block',
                    'if': {'row_index': 'odd', 'background': 'red'}
                    }
             ),
    html.Div([
        dcc.Graph(id='my-scatter-plot')])
]
)

@tab1.callback(Output('my-table', 'children'), [Input('movie_list_input', 'value')])
def update_table(selected_movie):
    movie_list = nmr.userchoice_based_movie_recommendation(selected_movie)
    movie_list_op = movie_list
    return nmr.generate_table(movie_list_op)


@tab1.callback(Output('my-scatter-plot', 'figure'),  [Input('movie_list_input', 'value')])
def update_figure(selected_movie):
    movie_list2 = nmr.userchoice_based_movie_recommendation(selected_movie)
    traces = []
    for i in movie_list2.Movie_Title.unique():
        one_movie_info = movie_list2[movie_list2['Movie_Title'] == i]
        traces.append(dict(
            x=one_movie_info['Year_of_Release'],
            y=one_movie_info['%Match'],
            text=one_movie_info['Movie_Title'],
            mode='markers',
            opacity=0.7,
            marker={
                'size': 15,
                'line': {'width': 0.5, 'color': 'white'}
            },
            name=i
        ))

    return {
        'data': traces,
        'layout': dict(
            xaxis={'type': 'log', 'title': 'Year of Release'},
            yaxis={'title': '%Match'},
            margin={'l': 40, 'b': 40, 't': 10, 'r': 10},
            hovermode='closest',
            transition={'duration': 500}
        )
    }


if __name__ == '__main__':
    tab1.run_server(debug=True)

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
