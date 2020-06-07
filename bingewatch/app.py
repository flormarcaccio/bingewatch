"""
This is the main file that hosts the web-app. It has dash app initialization and callouts.
"""
import dash
from dash.dependencies import Input, Output
import dash_html_components as html
import dash_core_components as dcc
import choice_based_recommendation
import tab2
import netflix as nmr
import imdb

IMDB_PATH = 'data/processed/imdb_df.csv'
GENRES_PATH = 'data/processed/set_genres.pkl'
IMDB_DF = imdb.load_data(IMDB_PATH)

EXTERNAL_STYLESHEETS = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=EXTERNAL_STYLESHEETS)
app.config.suppress_callback_exceptions = True

colors = {
    'background': 'white',
    'background1': 'light blue',
    'text': 'black'
}

app.layout = html.Div(style={'backgroundColor': colors['background']},
                      children=[
                          html.H1(
                              children='Movie Recommendation: Get your next watch here!',
                              style={
                                  'textAlign': 'center',
                                  'color': colors['text']
                              }
                          ),
                          html.Div(
                              children='Get your next watch just by entering '
                                       'either your favorite movie or your preferred genre '
                                       'or any time period. Tell us your choice & we will find'
                                       'the relevant movies and/or tv series '
                                       'that will absolutely delight you! So, lets go!!\n\n',
                              style={
                                  'textAlign': 'center',
                                  'color': colors['text']
                              }
                          ),
                          dcc.Tabs(id="tabs-example", value='tab-1',
                                   children=[
                                       dcc.Tab(label='Choice based Recommendation',
                                               value='tab-1'),
                                       dcc.Tab(label='Genre/Time Based Recommendation',
                                               value='tab-2'),
                                   ]),
                          html.Div(id='tabs-content-display')
                      ])


@app.callback(Output('tabs-content-display', 'children'),
              [Input('tabs-example', 'value')])
def render_content(tab):
    """
    This function displays tabs based on user selection of tab
    """
    if tab == 'tab-2':
        return tab2.tab2_layout
    return choice_based_recommendation.choice_based_recommendation_layout


## Tab 1: choice_based_recommendation callback
@app.callback(Output('my-table', 'children'), [Input('movie_list_input', 'value')])
def update_table(selected_movie):
    """
    It returns the html table of top 10 movies
    Args:
        selected_movie: user input of movie title
    Returns: Html table of 10 movies
    """
    movie_list = nmr.userchoice_based_movie_recommendation(selected_movie)
    return nmr.generate_table(movie_list)


@app.callback(Output('my-scatter-plot', 'figure'), [Input('movie_list_input', 'value')])
def update_figure(selected_movie):
    """
    This returns bar plot of movies along match scores
    Args:
        selected_movie: user input of movie title
    Returns: Bar plot of movies & match %age
    """
    movie_list2 = nmr.userchoice_based_movie_recommendation(selected_movie)
    return {
        'data': [{'x': movie_list2['Movie Title'], 'y': movie_list2['Match%'], 'type': 'bar'}],
        'layout': dict(
            hovermode='closest',
            title='Top 10 Most Recommended',
            yaxis={'title': 'Match%'},
            margin={'l': 45, 'b': 150, 't': 40, 'r': 15}
        )
    }


## Tab2:Genre/Time Based_recommendation callback
@app.callback(
    Output('graph-with-slider', 'figure'),
    [Input('filter-checklist', 'value'),
     Input('year-slider', 'value'),
     Input('title-type', 'value'),
     Input('genre-dropdown', 'value')
     ])
def update_figure_tab2(selected_filters, selected_year, selected_type, selected_genre):
    """
    Returns bar plot of movies with their weighted average
    """
    genre_filtered = imdb.filter_selected(selected_filters, 'Genre')
    year_filtered = imdb.filter_selected(selected_filters, 'Year')

    final_df = imdb.filter_type(IMDB_DF, selected_type)
    if genre_filtered and selected_genre:
        final_df = imdb.filter_genre(final_df, selected_genre)
    if year_filtered and selected_year:
        final_df = imdb.filter_year(final_df, selected_year)

    final_df = imdb.filter_top10(final_df)

    return {
        'data': [{'x': final_df['primaryTitle'], 'y': final_df['weightedAverage'], 'type': 'bar'}],
        'layout': dict(
            hovermode='closest',
            # height = 500,
            title='Top 10 Most Popular',
            yaxis={'title': 'Weighted Average'})
    }


if __name__ == '__main__':
    app.run_server(debug=True)
