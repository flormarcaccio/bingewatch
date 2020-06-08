This file demonstrates how users can interact with our movie recommendation visualization tool.

## Accessing the tool

The visualization tool is hosted on Heroku, a cloud platform which allows applications to be accessed through a web browser. Users can access our tool by simply clicking the following link: [https://seds-bingewatch.herokuapp.com/](https://seds-bingewatch.herokuapp.com/). 

Alternately, the project can be run locally by users with the following code:  
```
git clone https://github.com/flormarcaccio/bingewatch.git
pip install -r requirements.txt
python run.py
```
After running this code, copy and paste the web address output on the terminal into a web browser to view the visualization.

## Getting started

Our interface consists of two tabs: the first displays a choice-based recommendation, while the second tab shows a filter-based recommendation. 

(picture of tab 1 here) (picture of tab 2 here)

### Use cases 

In the first use case, if a user is interested in a movie similar to another movie they already watched, they can type in or select a liked movie and receive a list of top 10 movies similarly liked by others. This functionality is available through the first tab of our visualization.

In the second use case, if a user wants to see the top 10 movies or shows of a particular year, they can use the slider to select their desired year, and a list of the top 10 recommendations will be displayed. This functionality is available through the second tab of our visualization.

In the third use case, if a user wants to see the top 10 movies or shows of a particular genre, they can select their desired genre from a dropdown, and a list of the top 10 recommendations will be displayed. This functionality is available through the second tab of our visualization.

The second tab also allows users to select combinations of years and genres, as well as whether the user is interested in movies or TV shows.

### Filter options

Within the second tab, users can filter on whether they want to view movies or TV shows, which genres they are interested in, and which year the movie or show should be from.

(picture of filters here)

## Examples

### Case 1
Assume a user's favorite movie is Fight Club, and they want to see movies that are similar to it.
They can obtain recommendations using our tool by following these steps:
1. Select tab 1, "Choice Based Recommendation"
2. Click on the drop-down and begin typing the name of the movie
3. Select it in the alphabetized list within the drop-down
4. Recommendations will be shown!

(example 1 here)

### Case 2
Assume a user wants to get caught up on last year's hottest movies.
They can obtain recommendations using our tool by following these steps:
1. Select tab 2, "Filter Based Recommendation"
2. Deselect the checkbox for "Genre", leaving only the box for "Year" checked
3. Use the year slider to select the appropriate year, in this case 2019
4. Recommendations will be shown!

(example 2 here)

### Case 3
Assume a user is interested in binge-watching the most popular science fiction shows.
They can obtain recommendations using our tool by following these steps:
1. Select tab 2, "Filter Based Recommendation"
2. Deselect the checkbox for "Year", leaving only the box for "Genre" checked
3. Change the type of content shown from "Movie" to "TV Series" using the bubble selector
4. Use the drop-down to find and click on the genre name "Sci-Fi"
5. Recommendations will be shown!

(example 3 here)

### Case 4
Assume a user is interested in the top comedy movies from the year 2010.
They can obtain recommendations using our tool by following these steps:
1. Select tab 2, "Filter Based Recommendation"
2. Use the year slider to select the year 2010
3. Use the drop-down to find and click on the genre name "Comedy"
4. Recommendations will be shown!

(example 4 here)