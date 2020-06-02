# Unit tests for helper_functions.py
import pandas as pd
import unittest
import pickle
import os
import sys
sys.path.append('../data')
from bingewatch.data.helper_functions import *
from bingewatch.imdb import *


class test_df(unittest.TestCase):
	"""
	Check that the unique genres in the test_df
	have been correctly identified.
	"""
	test_df = pd.DataFrame({'movies' : ["A", "B", "C", "D"], 
			'genres' : ["Action", "Comedy", "Comedy", "Romance"]})

	def test_unique_genres(self):
		self.assertEqual(
			get_unique_genres(self.test_df), 
			set(["Action", "Comedy", "Romance"]))

	def test_save_file(self):
		"""
		Check that the save_file function correctly outputs a csv file,
		then remove the created file.
		"""
		save_file(self.test_df, "./", "test_file", ".csv")
		self.assertTrue(os.path.exists('./test_file.csv'))
		os.system("rm test_file.csv")

	def test_download_netflix_data(self):
		pass

	def test_parse_data(self):
		pass

	def test_get_recommended_movies(self):
		pass

	def test_format_movie_titles(self):
		pass

	def test_download_gz_file(self):
		pass

	def test_clean_imdb_data(self):
		pass




class test_imdb(unittest.TestCase):

	test_df = pd.DataFrame({
		'movies' : ["A", "B", "C", "D", "E", "F",
            "G", "H", "I", "J", "K"], 
		'titleType': ["Movie", "Movie", "Movie", "tvSeries",
		    "tvSeries", "tvSeries", "tvSeries", "Movie",
		    "tvSeries", "Movie", "Movie"],
        'genres' : ["Action", "Comedy", "Comedy", "Romance",
            "Comedy, Romance", "Comedy, Action", "Romance",
            "Action, Comedy", "Action", "Action", "Romance"],
        'startYear':[2020, 2019, 2018, 2020, 2016, 2015, 2012,
            2017, 2016, 2019, 2018],
        'weightedAverage':[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]})

	def test_load_data(self):
		original_file = pd.read_csv('bingewatch/data/processed/imdb_df.csv')
		self.assertEqual(len(load_data('bingewatch/data/processed/imdb_df.csv')),
			len(original_file))

	def test_load_genres(self):
		with open('bingewatch/data/processed/set_genres.pkl', 'rb') as f:
			original_file = pickle.load(f)
		self.assertEqual(load_genres('bingewatch/data/processed/set_genres.pkl'),
			list(original_file))

	def test_filter_type(self):
		self.assertEqual(len(filter_type(self.test_df, 'Movie')), 6)

	def test_filter_genre(self):
		self.assertEqual(len(filter_genre(self.test_df, 'Action')), 5)

	def test_filter_year(self):
		self.assertEqual(len(filter_year(self.test_df, 2018)), 2)

	def test_filter_top10(self):
		self.assertGreater(filter_top10(self.test_df)['weightedAverage'].min(), 1)

	def test_filter_genre(self):
		self.assertTrue(filter_selected(["tvSeries", "Movie"], "Movie"))




class test_netflix(unittest.TestCase):

	def test_reading_movie_title_csv(self):
		pass

	def test_get_options(self):
		pass

	def test_userchoice_based_movie_recommendation(self):
		pass

	def test_generate_table(self):
		pass




if __name__ == '__main__':
    unittest.main() 
