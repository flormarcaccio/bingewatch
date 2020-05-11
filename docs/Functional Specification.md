# Functional Specification
### Background

With the current advancements of so many online streaming websites for movies, one can now watch any movie old and new. However, with such a sheer volume of movies, it becomes overwhelming to browse among them and find a movie of one’s choice and taste. We intend to build a collaborative filtering-based recommendation system that provides recommendations based on similar profiles of its users. The goal is to provide a personalized streaming experience based on the user’s preference and liking. 

One key advantage of collaborative filtering is that it is independent of product knowledge. Rather, it relies on the users with a basic assumption that what the users liked in the past will also be liked in the future. For example, if a person A watches crime, sci-fi, and thriller genres and B watches sci-fi, thriller, and action genres then A will also like action, and B will like crime genre.

### User Profile

Users are anyone interested in streaming movies online or are looking for recommendations for their next watch. Users should be somewhat tech-savvy and familiar with web browser interactions such as hover, click, select from a menu, etc, so they must be able to interact with our recommender tool on a website or Shiny app. Alternatively, since the tool will also be available through Github, more technical users could clone the git repository and run a Python script to interact with the tool.

### Data Sources

| Title | Location | Features | Highlights |
 :---- | :--- | :--- | :----- |
Netflix Training Dataset | __[Netflix Prize Data](https://www.kaggle.com/netflix-inc/netflix-prize-data)__: Training_set.rar | user_id, movie, date of grade, grade| It contains a training data set of  100,480,507 ratings that 480,189 users gave to 17,770 movies.|
Netflix Movie Information Dataset | __[Netflix Prize Data](https://www.kaggle.com/netflix-inc/netflix-prize-data#movie_titles.csv):__ movie_titles.txt | Movie_id, year of release, title | It contains details for around 17,770 movies | 
IMDB’s Dataset |__[IMDB Data Files](https://www.imdb.com/interfaces/):__ title.basics.tsv.gz, title.ratings.tsv.gz | Genre of movie, start year, movie run time (minutes) |This dataset will be used to recommend a movie based on the genre selected by the user

### Use Cases

##### Use Case #1: The user wants to see movies similar to a liked movie
- User: User inputs his/her liked movie
- Tool: Based on the user’s liked movie, a list of recommended movies will be displayed

##### Use Case #2: The user wants to see the top 10 movies of a particular year 
- User: User inputs a particular year
- Tool: A list of the top 10 most recommended movies will be displayed

##### Use Case #3: The user wants to see the top 10 movies from a particular genre 
- User: User inputs the genre from a drop-down menu
- Tool: A list of the top 10 most recommended movies from that genre will be displayed


