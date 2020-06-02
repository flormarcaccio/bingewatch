import dash
import dash_html_components as html
import dash_core_components as dcc
import pandas as pd
import imdb
from dash.dependencies import Input, Output


IMDB_PATH = 'data/processed/imdb_df.csv'
GENRES_PATH = 'data/processed/set_genres.pkl'
df_imdb = imdb.load_data(IMDB_PATH)
genres = imdb.load_genres(GENRES_PATH)


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

tab2.layout = html.Div([
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

            html.Div([
                html.Label('Filter by:'),
                dcc.Checklist(
                        id = 'filter-checklist',
                        options=[
                            {'label': 'Genre', 'value': 'Genre'},
                            {'label': 'Year', 'value': 'Year'}
                        ],
                        value=['Genre', 'Year']
                    )

                ],
                style={'margin-bottom': '50px',
                        'margin-left':'20px'}),

            html.Div(id = 'slider-wrapper', children = 
             [
                html.Label('Year:'),
                 dcc.Slider
                (
                    id='year-slider',
                    min = int(df_imdb['startYear'].min()),
                    max = int(df_imdb['startYear'].max()),
                    value = int(df_imdb['startYear'].max()),
                    included=False,
                    updatemode = 'drag',
                    tooltip = {'always_visible': True}
                ),
            ],
            style={'margin-bottom': '50px',
                   'margin-left': '20px',
                   'margin-right': '20px',
                   'text-orientation': 'mixed'}),
        
        html.Div([  
            html.Div([
                html.Label('Select the genre you would like to see:'),
                    dcc.Dropdown(
                     id = 'genre-dropdown',
                     options = [{'label': i, 'value': i} for i in genres],
                     placeholder = 'Select Genre',
                 )],
                    style={'width': '48%',
                            'margin-bottom': '50px',
                            'margin-left':'20px',
                            'display': 'inline-block'}
            ),
               
            html.Div([
                html.Label('Select the type of content you would like to see:'),
                    dcc.RadioItems(
                        id='title-type',
                        options = [{'label': 'Movie', 'value' : 'movie'},
                                    {'label' :'TV Series', 'value': 'tvSeries'}],
                        value='movie',
                        labelStyle={'display': 'inline-block', 'padding': '10px'}
                )],
                    style={'width': '48%', 'float': 'right', 'display': 'inline-block'}
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
    [Input('filter-checklist', 'value'),
    Input('year-slider', 'value'),
    Input('title-type', 'value'),
    Input('genre-dropdown', 'value')
   ])

  
def update_figure(selected_filters, selected_year, selected_type, selected_genre):

    genre_filtered = imdb.filter_selected(selected_filters, 'Genre')
    year_filtered = imdb.filter_selected(selected_filters, 'Year')
    
    final_df = imdb.filter_type(df_imdb, selected_type)


    if genre_filtered and selected_genre:
        final_df = imdb.filter_genre(final_df, selected_genre)
    if year_filtered and selected_year:
        final_df = imdb.filter_year(final_df, selected_year)

    final_df = imdb.filter_top10(final_df)



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