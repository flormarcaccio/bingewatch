import dash
import dash_html_components as html
import dash_core_components as dcc
import plotly.graph_objects as go
import pandas as pd
from dash.dependencies import Input, Output
import numpy as np
import pickle
import dash_table

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

## Reading movie_title.csv for movie list dropdown
movielist = pd.read_csv("/Users/mansirathod/Documents/Quarter_StudyMaterial/Spring2020/SoftwareDesign/movie_titles_v2.csv", sep=",", encoding='latin-1')
movielist.head()
movielist.sort_values(by='Final_title',ascending=True, inplace=True)

## Setting up a dummy dataframe
selected_movie = 'A Christmas Carol'
mv_id = movielist[movielist['Final_title'] == selected_movie]
mvid_list = np.array(mv_id['Sno'])[0]
##Calling the movie recommendation algorithm
dict_rec = {}
with open('/Users/mansirathod/Documents/Quarter_StudyMaterial/Spring2020/SoftwareDesign/movie-recommendation-system/data/dict_recommendations.pkl', 'rb') as f:
    dict_rec = pickle.load(f)
df_final11 = movielist.loc[dict_rec[mvid_list][0][:10]]

#pd.read_csv("https://raw.githubusercontent.com/flormarcaccio/movie-recommendation-system/master/data/movie_titles.csv")

# Initialize the app
app = dash.Dash(__name__)
app.config.suppress_callback_exceptions = True

colors = {
    'background': '#665544',
    'background1': '#112233',
    'text': '#7FBDFF'
}


## Setting up function for our dropdowns: movie_list, year_list, genre list
def get_options(list_stocks):
    dict_list = []
    for i in list_stocks:
        dict_list.append({'label': i, 'value': i})

    return dict_list

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
    html.Div(className='eight columns div-user-controls',
             children=[
                 html.H4(children='Enter a movie you have loved watching: ',
                         style={
                             'textAlign': 'left',
                             'color': colors['text']
                         }),
                 html.Div(
                     className='div-for-dropdown',
                     children=[
                         dcc.Dropdown(id='movielist_input', options=get_options(movielist['Final_title'].unique()),
                                       multi =True, value=[movielist['Final_title'][11940]],
                                      style={'backgroundColor': colors['background']},
                                      className='movielist_input', searchable=True
                                      ),
                         dash_table.DataTable(id="new_datatable")
                     ],
                     style={
                         'textAlign': 'left',
                         'color': colors['text']
                     }
                 )

             ]
             ),
    ]
)

@app.callback(Output('new_datatable', 'rows'),[Input('movielist_input', 'value')])
def update_figure(selected_movie):
    movie_id = movielist['Final_title' == selected_movie][0]
    mv_id = movielist[movielist['Final_title'] == selected_movie]
    mvid_list = np.array(mv_id['Sno'])[0]
    ##Calling the movie recommendation algorithm
    dict_rec = {}
    with open(
            '/Users/mansirathod/Documents/Quarter_StudyMaterial/Spring2020/SoftwareDesign/movie-recommendation-system'
            '/data/dict_recommendations.pkl','rb') as f:
        dict_rec = pickle.load(f)

    df_final = movielist.loc[dict_rec[mvid_list][0][:10]]
    return df_final.to_dict('records')


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