# -*- coding: utf-8 -*-
"""
Created on Mon May 18 17:52:12 2020

@author: Sanjana
"""

import pandas as pd
import pickle


def load_data():
    imdb_df = pd.read_csv('data/processed/imdb_df.csv')
    return imdb_df

def load_genres():
    with open('data/processed/set_genres.pkl', 'rb') as f:
        genres_set = pickle.load(f)
    return list(genres_set)

def filter_type(data, titletype:str):
    return data[data['titleType'].str.contains(titletype)]
    

def filter_genre(data, genre:str):
    return data[data['genres'].str.contains(genre)]

def filter_year(data, yr:int):
    return data[data['startYear'].astype(int) == yr]

def filter_top10(data):
    return data.nlargest(10, 'weightedAverage')

def filter_selected(list_values, value):
    return value in list_values