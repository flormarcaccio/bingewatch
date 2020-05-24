from datetime import datetime
import pandas as pd
import numpy as np
from scipy import sparse
from sklearn.metrics.pairwise import cosine_similarity
import pickle

# Process Netflix data
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
    
    return final_list

# Load all four files with movie ratings
startTime = datetime.now()

data = formatting_data('raw-data/combined_data_1.txt')
data += formatting_data('raw-data/combined_data_2.txt')
data += formatting_data('raw-data/combined_data_3.txt')
data += formatting_data('raw-data/combined_data_4.txt')

df_netflix = pd.DataFrame(data, columns = ['movie_id', 'user_id', 'rating', 'rating_date'])
df_netflix.to_csv('netflix-prize-data/netflix_data.csv')

print(len(data))
del data
print(datetime.now() - startTime)

# Explore data
print("Data info:")
print("Total number of ratings = "+str(df_netflix.shape[0]))
print("Unique movies = "+str(len(np.unique(df_netflix["movie_id"]))))
print("Unique users = "+str(len(np.unique(df_netflix["user_id"]))))
print("Duplicated rows = "+str(df_netflix.duplicated(["movie_id","user_id", "rating"]).sum()))
print("Number of NaN values = "+str(df_netflix.isnull().sum()))

# Creating sparse matrix and calculating similarity between movies
sparse_data = sparse.csr_matrix((df_netflix.rating, (df_netflix.user_id, df_netflix.movie_id)))
similarity = cosine_similarity(sparse_data.T, dense_output = False)

# Creating a dictionary with all the similar movies
movie_ids = np.unique(similarity.nonzero())
similar_movies_dict = dict()
for movie in movie_ids:
    rec_movies = np.argsort(-similarity[movie].toarray().ravel())[1:100]
    similar_movies_dict[movie] = rec_movies

# Storing dictionary in data folder
with open('data/dict_recommendations.pkl', 'wb') as f:
    pickle.dump(similar_movies_dict, f, protocol=pickle.HIGHEST_PROTOCOL)

# Process IMDB data
# Loading raw data from https://datasets.imdbws.com/
df_imdb_ratings = pd.read_csv('raw-data/title.ratings.tsv', sep = '\t', na_values=['\\N'])
df_imdb_titles = pd.read_csv('raw-data/title.basics.tsv', sep = '\t', na_values=['\\N'])

# Keeping only movies and series
df_imdb_titles = df_imdb_titles[df_imdb_titles.titleType.isin(['movie', 'tvSeries'])][['tconst', 'titleType', 'primaryTitle', 'startYear', 'genres']]

# Merging both sets, removing rows with no rating, genre or startYear, and adding weighted average
df_imdb = df_imdb_titles.merge(df_imdb_ratings, how='left', left_on='tconst', right_on='tconst')
df_imdb['titleType'] = df_imdb['titleType'].astype(str)
df_imdb = df_imdb.dropna()
df_imdb['weightedAverage'] = df_imdb['averageRating']*df_imdb['numVotes']

# Storing final IMDb dataframe in the Data directory
df_imdb.to_csv('data/imdb_df.csv', index = False)

# Storing set of possible genres
genres_raw = list(df_imdb['genres'].unique())
genres = set([element for item in genres_raw for element in item.split(',')])
with open('data/set_genres.pkl', 'wb') as f:
    pickle.dump(genres, f, protocol=pickle.HIGHEST_PROTOCOL)

