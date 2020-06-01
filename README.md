[![Build Status](https://travis-ci.com/flormarcaccio/movie-recommendation-system.svg?branch=master)](https://travis-ci.com/flormarcaccio/movie-recommendation-system)

# [UW DATA 515A](http://uwseds.github.io/grading.html) - Software Engineering for Data Scientists
  
## Final Project - Movie Recommendation System

### Team Members - Bianca Zlavog, Florencia Marcaccio, Mansi Rathod, Sanjana Gupta


## Project Summary
With the current advancements of so many online streaming websites for movies, one can now watch any movie or show old and new. However, with such a sheer volume of movies, it becomes overwhelming to browse among them and find a movie of one’s choice and taste. We have built a collaborative filtering-based recommendation system that provides movie and TV show suggestions based on similar profiles of its users. The goal is to create a personalized streaming experience based on the user’s preference and liking. 

In our first use case, the user wants to see movies similar to a liked movie. For this, we leverage the Netflix prize dataset and calculate the cosine similarity between all entries in a item-item matrix to obtain the movies with highest similarity scores to the user's input movie. In another use case, the user wants to see the top 10 movies from a particular genre or year. Here we employ the IMDB movie datasets and subset to the user specifications to obtain a list of the top movies based on rating score wighted by the number of ratings.

Finally, we provide a visualization tool for users to access our recommender system through a web application built in Dash.

## Input Data
- [IMDB movie data](https://datasets.imdbws.com/). We use the `title.ratings` and `title.basics` to obtain movie and TV show ratings and titles, as well as the information on genre and release year.

- [Netlix prize data](https://www.kaggle.com/netflix-inc/netflix-prize-data). This dataset is available through Kaggle, and contains user IDs, movie IDs, ratings, and movie titles.

## Data Processing

- The preproccessing of the data is handled by `data_manager.py`. The package does not run this module, as the data was processed in advance and has already been output for use. However, if you want to run this script yourself you will need to follow the steps described below to download the "Netflix Prize Data" dataset, as it is stored on Kaggle.  
  
<details>
Option 1:

- Manually download the dataset from the Kaggle website, and unzip the folder `netflix-prize-data` in the /movie-recommendation-system/data directory, at the same level as data_manager.py.
- Comment the line 18 from *data_manager.py*, so that it appear like:
`#hf.download_netflix_data(NF_KAGGLE_USER, NF_DIRECTORY)`
  
Option 2:
- Install the kaggle package from the terminal: `pip install kaggle`
- Download the API Token from Kaggle: Go to [Kaggle website](https://www.kaggle.com/) -> Account -> API -> Create New API Token. This will download a json file with the following format: `{"username”:string_username,”key”:string_key}`
- Place the json file into the hidden `.kaggle/` folder, created when you installed the package. If you cannot find this folder, run the command `kaggle` on your terminal. This will give you an error that looks like this: *“Could not find kaggle.json. Make sure it's located in path/to/the/.kaggle/directory.”* From there, you can get path where you are supposed to store your json file.
</details>

- `data_manager.py` reads in the movie data from both Netflix and IMDB data sources, keeps only variables and observations of interest, calculates movie similarity scores for the Netflix data and weighted ratings for the IMDB data, and outputs processed files for use in the visualization tool.

- `filename_here` produces the visualization tool which shows the top movie recommendations based on user input.

### License
This work is available under an MIT license, included in the repository.

### Software used
Python version x

Jupyter notebook version x

Operating system version x

