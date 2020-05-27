# DS
Data Science repository for Lambda School's PostHere build for classifying the proper Subreddit a post should go in using a Natural Language Processing model.

## Directory Structure
```
├── README.md  <- You are here! Data Science README file.
├── requirements.txt  <- The requirements file for reproducing environment.
├── data
│    ├── datasets          <- CSV files of Fetched / Cleaned Data
│    │     ├── cleaned_data.csv <- CSV output of clean_preprocess.py
│    │     └── fetched_data.csv <- CSV output of fetch_data.py
│    ├── clean_preprocess.ipynb  <- Cleaning / tokenizing final data for usage in modeling.  (TODO: .py, functional as .ipynb)
│    └── fetch_data.ipynb  <- Fetches data using Reddit's API for technical support subreddits.  (TODO: .py, functional as .ipynb)
└──  modeling
│    ├── predict.py <- Makes multi-class classification prediction on which Subreddit to post in.  (TODO)
│    └── train_model.py <- Trains our model for use in predict.py  (TODO)
└──data_engineering <- Directory to store data engineering progress 
     ├── routes <- Create routes to important data pages
     │      ├── home_routes.py <- Create route to home page
     │      └── predict_routes.py <- Create route to predict page
     ├── models.py <- models for database, classes, helper methods, etc
     └── __init__.py <- init file...main file where app is created and run
```