import dash
import dash_html_components as html
import dash_core_components as dcc
import pandas as pd
import helper_functions
import imdb
from dash.dependencies import Input, Output

df = pd.read_csv('./data/imdb_df.csv')

genres = list(helper_functions.get_unique_genres(df))
year = list((df['startYear'].unique()).astype(int))

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    dcc.Tabs(id='tabs-example', value='tab-1', children=[
        dcc.Tab(label='Movie Recommendation System', value='tab-1'),
        dcc.Tab(label='Top 10 Based on Genre/Year', value='tab-2', children = [
            html.Div(
                [
                    html.P('Get the top 10 most popular movies based on your selection.')
                ], 
                style={'marginBottom': 30, 
                       'marginTop': 25, 
                       'fontSize':18}),
            html.Div(id = 'slider-wrapper', children = 
             [
                html.Label('Year:'),
                 dcc.Slider
                (
                    id='year-slider',
                    #min=df['startYear'].min(),
                    #max=df['startYear'].max(),
                    min = int(df['startYear'].min()),
                    max = int(df['startYear'].max()),
                    value = int(df['startYear'].max()),
                    #marks={str(startYear): str(startYear) for startYear in year},
                    included=False,
                    #step=1000,
                    updatemode = 'drag',
                    tooltip = {'always_visible': True}
                ),
            ],
            style={'margin-bottom': '50px',
                   'margin-left': '20px',
                   'margin-right': '20px',
                   'text-orientation': 'mixed'}),
      html.Div([dcc.Markdown('Select the genre you would like to see:'),
                ]),
        
        html.Div([  
            html.Div([
                #html.Label('Select the genre you would like to see:'),
                    dcc.Dropdown(
                     id = 'genre-dropdown',
                     options = [{'label': i, 'value': i} for i in genres],
                     #multi = True,
                     #value = 'Action',
                     placeholder = 'Select Genre',
                     #style={'height': '40px', 'width': '300px', 'align-items': 'center', 'justify-content':'center'}
                 )
                 ], 
                style={'height': '60px', 
                   'width': '500px',
                   'marginTop': 15, 
                   'fontSize':15, 
                   'text-align': 'center',
                   'display' : 'inline-block'
                   }),
               
            html.Div([
            html.Label('Select the type of content you would like to see:'),
                dcc.RadioItems(
                    id='title-type',
                    #options=[{'label': i, 'value': i} for i in df['titleType'].unique()],
                    options = [{'label': 'Movie', 'value' : 'movie'},
                                {'label' :'TV Series', 'value': 'tvSeries'}],
                    value='movie',
                    labelStyle={'display': 'inline-block', 'padding': '10px'}
            )],
        style={ 'height' : '60px',
               'width' : '800px',
                'display' : 'inline-block',
               'text-align': 'center',
               'marginTop': 15, 
               'fontSize':15}
        ),
        ]),
        html.Div([
            dcc.Graph(style={'height': '400px', 
                             'width': '1300px', 
                             'margin-left':'auto', 
                             'margin-right':'auto'},
                      id='graph-with-slider')
                ])
            ])
        ]),
   ])
    
@app.callback(
    Output('graph-with-slider', 'figure'),
    [Input('year-slider', 'value'),
    Input('title-type', 'value'),
    Input('genre-dropdown', 'value')
   ])

  
def update_figure(selected_year, selected_type, selected_genre):
    if selected_genre and selected_year:
        movie_df = imdb.genre_year_df(selected_genre, selected_year, selected_type)
        final_df = movie_df
        #print(movie_df)
    elif selected_genre:
        genre_df = imdb.genre_df(selected_genre, selected_type)
        final_df = genre_df
        #print(genre_df)    
    elif selected_year:
        year_df = imdb.year_df(selected_year, selected_type)
        final_df = year_df
       # print(year_df)
    return {
        'data': [{'x': final_df['primaryTitle'], 'y' : final_df['weightedAverage'], 'type' : 'bar'}],
        'layout': dict(
            hovermode = 'closest',
            #height = 500,
            title = 'Top 10 Most Popular',
            yaxis = {'title': 'Weighted Average'}
        )
    }


if __name__ == '__main__':
    app.run_server(debug=True)