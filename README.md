# UW DATA 515A - Software Engineering for Data Scientists
  
## Final Project - Netflix Recommendations System

[Netlix dataset source](https://www.kaggle.com/netflix-inc/netflix-prize-data)

##### Team Members: Bianca Zlavog, Florencia Marcaccio, Mansi Rathod, Sanjana Gupta

#### Background
With the current advancements of so many online streaming websites for movies, one can now watch any movie old and new. However, with such a sheer volume of movies, it becomes overwhelming to browse among them and find a movie of one’s choice and taste. We intend to build a collaborative filtering-based recommendation system that provides recommendations based on similar profiles of its users. The goal is to provide a personalized streaming experience based on the user’s preference and liking. 

One key advantage of collaborative filtering is that it is independent of product knowledge. Rather, it relies on the users with a basic assumption that what the users liked in the past will also be liked in the future. For example, if a person A watches crime, sci-fi, and thriller genres and B watches sci-fi, thriller, and action genres then A will also like action, and B will like crime genre.


## Data Manager
The package does not run this module, as the data was processed in advance. However, if you want to run `data_manager.py` yourself you will need to follow some steps to download the "Netflix Prize Data" dataset, as it is stored on Kaggle.  
  
**Option 1:**  

* Manually download the dataset from the [Kaggle website](https://www.kaggle.com/netflix-inc/netflix-prize-data), and unzip the folder `netflix-prize-data` in the main directory of the repository.
* Comment the line 18 from *data_manager.py*, so that it appear like:
`#hf.download_netflix_data(NF_KAGGLE_USER, NF_DIRECTORY)`
  
**Option 2:**
* Install the kaggle package from the terminal: `pip install kaggle`
* Download the API Token from Kaggle: Go to [Kaggle website](https://www.kaggle.com/) -> Account -> API -> Create New API Token. This will download a json file with the following format: `{"username”:string_username,”key”:string_key}`
* Place the json file into the hidden `.kaggle/` folder, created when you installed the package. If you cannot find this folder, run the command `kaggle` on your terminal. This will give you an error that looks like this: *“Could not find kaggle.json. Make sure it's located in path/to/the/.kaggle/directory.”* From there, you can get path where you are supposed to store your json file.


