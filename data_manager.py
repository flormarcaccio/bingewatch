"""
This module executes the preprocessing of the datasets obtained from the
IMDb website and the Netflix Prize Dataset from Kaggle. Please look at
the instructions on how to obtain the Netflix dataset before executing
this script.
"""
import shutil

import pandas as pd

import helper_functions as hf

# NETFLIX
# Download the files, unzip them and get the data in a dataframe.
NF_KAGGLE_USER = 'netflix-inc'
NF_DIRECTORY = 'netflix-prize-data'
hf.download_netflix_data(NF_KAGGLE_USER, NF_DIRECTORY)

LIST_NF_DATA = []
FILE_I = list(range(1, 5))
FILE_PATH = NF_DIRECTORY+'/combined_data_'
LIST_NF_FILES = [FILE_PATH+str(i)+'.txt' for i in FILE_I]
for file in LIST_NF_FILES:
    LIST_NF_DATA += hf.parse_data(file)
DF_NF_COLS = ['movie_id', 'user_id', 'rating', 'rating_date']
DF_NETFLIX = pd.DataFrame(LIST_NF_DATA, columns=DF_NF_COLS)

# Get the movie recommendation dictionary and store in data folder.
DICT_RECOMMENDATIONS = hf.get_recommended_movies(DF_NETFLIX)
hf.save_file(DICT_RECOMMENDATIONS, 'data/', 'dict_recommendations', '.pkl')

# Cleaning the movie_titles file
TITLES_PATH = NF_DIRECTORY+'/movie_titles.csv'
DF_TITLES = hf.format_movie_titles(TITLES_PATH)
hf.save_file(DF_TITLES, 'data/', 'movie_titles', '.csv')

#Deleting original Netflix dataset directory
shutil.rmtree(NF_DIRECTORY)

# IMDB
# Download the data and store the cleaned and merged datasets.
IMDB_TITLES_URL = 'https://datasets.imdbws.com/title.basics.tsv.gz'
IMDB_RATINGS_URL = 'https://datasets.imdbws.com/title.ratings.tsv.gz'
DF_IMDB_TITLES = hf.download_gz_file(IMDB_TITLES_URL)
DF_IMDB_RATINGS = hf.download_gz_file(IMDB_RATINGS_URL)
DF_IMDB = hf.clean_imdb_data(DF_IMDB_TITLES, DF_IMDB_RATINGS)
hf.save_file(DF_IMDB, 'data/', 'imdb_df', '.csv')

# Get unique genres and storing them in data folder.
GENRES = hf.get_unique_genres(DF_IMDB)
hf.save_file(GENRES, 'data/', 'set_genres', '.pkl')
