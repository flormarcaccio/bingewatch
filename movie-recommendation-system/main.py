import dash
from dash.dependencies import Input, Output
import dash_html_components as html
import dash_core_components as dcc
import tab1
import tab2_dummy as tab2
import netflix as nmr

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
        'data': [{'x': movie_list2['Movie_Title'], 'y': movie_list2['%Match'], 'type': 'bar'}],
        'layout': dict(
            hovermode='closest',
            title='Top 10 Most Recommended',
            yaxis={'title': '%Match'},
            margin={'l': 45, 'b': 150, 't': 40, 'r': 15}
        )
    }


# Tab 2 callback
@app.callback(Output('my-table2', 'children'), [Input('movie_list_input2', 'value')])
def update_table(selected_movie):
    movie_list = nmr.userchoice_based_movie_recommendation(selected_movie)
    movie_list_op = movie_list
    return nmr.generate_table(movie_list_op)


app.css.append_css({
    'external_url': 'https://codepen.io/chriddyp/pen/bWLwgP.css'
})

if __name__ == '__main__':
    app.run_server(debug=True)