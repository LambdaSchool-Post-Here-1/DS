# DS
Data Science repository for Lambda School's PostHere build for classifying the proper technical support Subreddit a post should go in using a Natural Language Processing model. Our goal was to create a NLP model to classify the proper Subreddit a post should go into in under the span of a week. We worked cross-collaboratively with peers from other career tracks to complete this project.

## Directory Structure
```
├── README.md  <- You are here! Data Science README file.
├── requirements.txt  <- The requirements file for reproducing environment.
├── data <- Data collection, cleaning, preprocessing, CSV files.
│    ├── datasets          <- CSV files of Fetched / Cleaned Data
│    │     ├── cleaned_data.csv <- CSV output of clean_preprocess.py
│    │     └── fetched_data.csv <- CSV output of fetch_data.py
│    ├── clean_preprocess.py  <- Cleaning / tokenizing final data for usage in modeling.
│    └── fetch_data.py  <- Fetches data using Reddit's API for technical support subreddits.
└──  modeling
│    ├── predict.py <- Makes multi-class classification prediction on which Subreddit to post in. (TODO: Connect to model)
│    └── train_model.py <- Trains our model for use in predict.py  (TODO: Finish OOP)
└──data_engineering <- Directory to store data engineering progress
     ├── routes <- Create routes to important data pages
     │      ├── home_routes.py <- Create route to home page
     │      └── predict_routes.py <- Create route to predict page
     ├── models.py <- models for database, classes, helper methods, etc
     └── __init__.py <- init file...main file where app is created and run
```

**Contributors:**
Data Engineer - Daniel Benson
Machine Learning Engineer - Kenneth T. Barrett
