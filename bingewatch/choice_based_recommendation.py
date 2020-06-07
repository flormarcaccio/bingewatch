""" This is dash layout file for Personal Choice based Recommendation.
    It is being called in app.py
"""
import dash_html_components as html
import dash_core_components as dcc
import netflix as nmr

## Reading movie_title.csv for movie list dropdown
MOVIES_DF = nmr.reading_movie_title_csv()

COLORS = {
    'background': 'white',
    'background1': 'light blue',
    'text': 'black'
}

CHOICE_BASED_RECOMMENDATION_LAYOUT = html.Div(
    style={'backgroundColor': COLORS['background']}, children=[
        html.Div(className='div-user-controls',
                 children=[
                     html.H4(children='Enter a movie you have loved watching: ',
                             style={
                                 'textAlign': 'left',
                                 'color': COLORS['text']
                             }),
                     html.Div(
                         className='div-for-dropdown-and-table',
                         children=[
                             dcc.Dropdown(id='movie_list_input',
                                          options=nmr.get_options(MOVIES_DF['Display'].unique()),
                                          value=[MOVIES_DF['Display'].iloc[206]],
                                          searchable=True,
                                          placeholder="Select a movie"
                                          ),
                         ],
                         style={'width': '50%', 'text': 'black'}
                     ),
                     html.Div(children=[html.H1("\n \n")]),
                     html.Div(id='after_input_text',
                              children=[html.P("\n\nWe believe based on your liking "
                                               "for the above movie, the following "
                                               "10 movies will interest you the most:")],
                              style={'text-orientation': 'left'}
                              )
                 ]
                 ),
        html.Div(id='output',
                 className='row',
                 children=[html.Div(id='my-table',
                                    className='five columns'),
                           html.Div(dcc.Graph(id='my-scatter-plot'),
                                    className='seven columns')
                           ]
                 )
    ]
)
