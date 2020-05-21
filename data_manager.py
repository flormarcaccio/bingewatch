import pandas as pd
import numpy as np
from scipy import sparse
from sklearn.metrics.pairwise import cosine_similarity
import pickle



def formatting_data(file_path):
    f = open(file_path, 'rt')
    data = f.readlines()
    final_list = []
    for i, line in enumerate(data):
        if ':' in line:
            current_movie_id = int(line[:-2])
        elif ',' in line:
            tmp = line[:-1].split(',')
            final_list.append([current_movie_id, int(tmp[0]), int(tmp[1]), tmp[2]])
    print('Done parsing file: ', file_path)
    return final_list


def get_similar_movies(df):
    # Creating sparse matrix and calculating cosine similarity between movies
    sparse_data = sparse.csr_matrix((df.rating, (df.user_id, df.movie_id)))
    similarity = cosine_similarity(sparse_data.T, dense_output = False)
    # Creating a dictionary with the similar movies
    movie_ids = np.unique(similarity.nonzero())
    similar_movies_dict = dict()
    for movie in movie_ids:
        rec_movies_ids = np.argsort(-similarity[movie].toarray().ravel())[1:100]
        rec_movies_score = np.array(sorted(similarity[movie].toarray().ravel(), reverse = True)[1:100])
        similar_movies_dict[movie] = [rec_movies_ids, rec_movies_score]
    print('Finished creating cosine similarity dictionary')
    return similar_movies_dict


def cleaning_imdb_data(df_titles, df_ratings):
    df_titles = df_titles[df_titles.titleType.isin(['movie', 'tvSeries'])][['tconst', 'titleType', 'primaryTitle', 'startYear', 'genres']]
    df_imdb = df_titles.merge(df_ratings, how='left', left_on='tconst', right_on='tconst')
    df_imdb['titleType'] = df_imdb['titleType'].astype(str)
    df_imdb = df_imdb.dropna()
    df_imdb['weightedAverage'] = df_imdb['averageRating']*df_imdb['numVotes']
    print('Done cleaning and merging IMDb data')
    return df_imdb


def get_unique_genres(df):
    genres_all = list(df['genres'].unique())
    genres_unique = set([element for item in genres_all for element in item.split(',')])
    return genres_unique



##################

# NETFLIX

# Loading the data

data = []

files = ['raw-data/combined_data_1.txt', 'raw-data/combined_data_2.txt', 'raw-data/combined_data_3.txt', 'raw-data/combined_data_4.txt']
for file in files:
    data += formatting_data(file)

df_netflix = pd.DataFrame(data, columns = ['movie_id', 'user_id', 'rating', 'rating_date'])


# Getting the movie recommendation dictionary and storing in data folder

dict_recommendations = get_similar_movies(df_netflix)
with open('data/dict_recommendations.pkl', 'wb') as f:
    pickle.dump(dict_recommendations, f, protocol=pickle.HIGHEST_PROTOCOL)
print('Dictionary with movie recommendations is stored in the data folder')


##################

# IMDB

# Loading the data

df_imdb_titles = pd.read_csv('raw-data/title.basics.tsv', sep = '\t', na_values=['\\N'])
df_imdb_ratings = pd.read_csv('raw-data/title.ratings.tsv', sep = '\t', na_values=['\\N'])


# Cleaning and merging data, and storing in data folder

df_imdb = cleaning_imdb_data(df_imdb_titles, df_imdb_ratings)
df_imdb.to_csv('data/imdb_df.csv', index = False)
print('IMDb data is stored in the data folder')

# Getting unique genres and storing them in data folder

genres = get_unique_genres(df_imdb)
with open('data/set_genres.pkl', 'wb') as f:
    pickle.dump(genres, f, protocol=pickle.HIGHEST_PROTOCOL)






