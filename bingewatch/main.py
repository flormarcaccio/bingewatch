import dash
from dash.dependencies import Input, Output
import dash_html_components as html
import dash_core_components as dcc
import tab1
import tab2
import netflix as nmr
import imdb

IMDB_PATH = 'data/processed/imdb_df.csv'
GENRES_PATH = 'data/processed/set_genres.pkl'
df_imdb = imdb.load_data(IMDB_PATH)
genres = imdb.load_genres(GENRES_PATH)

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
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
                              children='This is a movie recommendation webpage. Get your next watch just by entering either your '
                                       'favorite movie. You are also free to enter your most liked genre or year of watch and we will '
                                       'find the most relevant movies and/or tv series that will absolutely delight you! So, lets go!!',
                              style={
                                  'textAlign': 'center',
                                  'color': colors['text']
                              }
                              ),
                          dcc.Tabs(id="tabs-example", value='tab-1',
                                   children=[
                                       dcc.Tab(label='Personal Choice Based Recommendation', value='tab-1'),
                                       dcc.Tab(label='Genre/Time Based Recommendation', value='tab-2'),
                                   ]),
                          html.Div(id='tabs-content-display')
                      ])


@app.callback(Output('tabs-content-display', 'children'),
              [Input('tabs-example', 'value')])

def render_content(tab):
    if tab == 'tab-1':
        return tab1.tab1_layout
    elif tab == 'tab-2':
        return tab2.tab2_layout


# Tab 1 callback
@app.callback(Output('my-table', 'children'), [Input('movie_list_input', 'value')])
def update_table(selected_movie):
    movie_list = nmr.userchoice_based_movie_recommendation(selected_movie)
    return nmr.generate_table(movie_list)


@app.callback(Output('my-scatter-plot', 'figure'), [Input('movie_list_input', 'value')])
def update_figure(selected_movie):
    movie_list2 = nmr.userchoice_based_movie_recommendation(selected_movie)
    traces = []
    return {
        'data': [{'x': movie_list2['Movie Title'], 'y': movie_list2['Match%'], 'type': 'bar'}],
        'layout': dict(
            hovermode='closest',
            title='Top 10 Most Recommended',
            yaxis={'title': 'Match%'},
            margin={'l': 45, 'b': 150, 't': 40, 'r': 15}
        )
    }


# Tab 2
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


app.css.append_css({
    'external_url': 'https://codepen.io/chriddyp/pen/bWLwgP.css'
})

if __name__ == '__main__':
    app.run_server(debug=True)
