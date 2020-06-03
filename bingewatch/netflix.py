import pickle
import os
import pandas as pd
import numpy as np
import dash_html_components as html

def reading_movie_title_csv():
    movies_df = pd.read_csv("data/processed/movie_titles.csv", sep=",")
    movies_df.sort_values(by='Final_title', ascending=True, inplace=True)
    return movies_df

## Setting up function for our dropdowns: movie_list, year_list, genre list
def get_options(movies_df):
    """
    List all the unique elements of a column in dropdown
    Args:
        movie_list: Final_title
    Returns: list of columns
    """
    dict_list = []
    for i in movies_df:
        dict_list.append({'label': i, 'value': i})
    print(type(dict_list))
    dict_list.pop()
    return dict_list


def userchoice_based_movie_recommendation(selected_movie):
    movies_df = pd.read_csv("data/processed/movie_titles.csv", sep=",")
    if type(selected_movie) is list:
        movie_details = movies_df[movies_df['Display'] == selected_movie[0]]
    else:
        movie_details = movies_df[movies_df['Display'] == selected_movie]
    movie_id = movie_details['Sno'].iloc[0]
    ##Calling the movie recommendation algorithm
    dict_rec = {}
    with open("data/processed/dict_recommendations.pkl", 'rb') as f:
        dict_rec = pickle.load(f)
    # print(dict_rec[movie_id_list])
    recommended_movie_ids = dict_rec[movie_id][0][:10]
    recommended_movie_scores = dict_rec[movie_id][1][:10]
    top10_movies = movies_df[movies_df.Sno.isin(recommended_movie_ids)]
    top10_movies['Match%'] = recommended_movie_scores
    top10_movies['Match%'] = round(round(top10_movies['Match%'],2)*100)
    top10_movies = top10_movies.drop(['Sno', 'Display'], axis=1)
    top10_movies.columns = ['Year of Release','Movie Title', 'Match%']
    # movie_list = movie_list[dict_rec[movie_id][0][:10]]  ##//compilation error
    # movie_list = movie_list.head(10)
    return top10_movies

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

