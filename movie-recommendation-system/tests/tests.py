# Unit tests for helper_functions.py
import pandas as pd
import unittest
import sys
sys.path.append('../data')
from helper_functions import *

class test_df(unittest.TestCase):
	# One-shot tests
	def one_shot_unique_genres(self):
		self.assertEqual(
			get_unique_genres(pd.DataFrame({'movies' : ["A", "B", "C", "D"], 
			'genres' : ["Action", "Comedy", "Comedy", "Romance"]})), 
			set(["Action", "Comedy", "Romance"]))


if __name__ == '__main__':
    unittest.main() 
