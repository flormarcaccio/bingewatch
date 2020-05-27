# -*- coding: utf-8 -*-
"""
Created on Mon May 18 17:52:12 2020

@author: Sanjana
"""

import pandas as pd

imdb_dt = pd.read_csv('data/imdb_df.csv')
imdb_dt['startYear'] = imdb_dt['startYear'].astype(int)

def matchGenre(genre:str):
  imdb_dt1 = imdb_dt[imdb_dt['genres']==genre]
  imdb_dt1 = imdb_dt1.sort_values(by='weightedAverage', ascending=False)
  movielist = imdb_dt1.primaryTitle.to_numpy()
  if len(movielist)>10:
    movielist = movielist[0:10]
  return movielist

def matchYear(yr:int):
  imdb_dt2 = imdb_dt[imdb_dt['startYear']==yr]
  imdb_dt2 = imdb_dt2.sort_values(by='weightedAverage', ascending=False)
  movielist2 = imdb_dt2.primaryTitle.to_numpy()
  if len(movielist2)>10:
    movielist2 = movielist2[0:10]
  return movielist2

def genre_df(genre:str, titletype:str):
    imdb_dt3 = imdb_dt[imdb_dt['genres'].str.contains(genre) 
                       & imdb_dt['titleType'].str.contains(titletype)]
    filtered_df = imdb_dt3.nlargest(10, 'weightedAverage')
    return filtered_df

def year_df(yr:int, titletype:str):
    imdb_dt4 = imdb_dt[imdb_dt['startYear'].astype(int) == yr]
    imdb_dt4 = imdb_dt4[imdb_dt4['titleType'].str.contains(titletype)]
    filtered_df = imdb_dt4.nlargest(10, 'weightedAverage')
    return filtered_df

def genre_year_df(genre:str, yr:int, titletype:str):
    imdb_dt5 = imdb_dt[(imdb_dt['genres'].str.contains(genre)) & 
                       (imdb_dt['titleType'].str.contains(titletype)) & 
                       (imdb_dt['startYear'].astype(int) == yr)]    
    #print(imdb_dt5)
    filtered_df = imdb_dt5.nlargest(10, 'weightedAverage')
    #print(filtered_df)
    return filtered_df

#genre_df('Action', 'tvSeries')
#print(year_df(2010, 'tvSeries'))
#print(genre_year_df('Action', 2010, 'tvSeries'))
#print(imdb_dt['startYear'].type)
