# DS
Data Science Repository for Post Here build week for Lambda School.

## Directory Structure:
├── README.md  <- You are here! Data Science README file.
├── requirements.txt  <- The requirements file for reproducing environment.
├── data
│    ├── datasets          <- CSV files of Fetched / Cleaned Data
│    │     ├── cleaned_data.csv <- CSV output of clean_data.py
│    │     └── fetched_data.csv <- CSV output of fetch_data.py
│    ├── clean_data.ipynb  <- Cleaning data for usage in modeling.  (TODO: .py, functional as .ipynb)
│    └── fetch_data.ipynb  <- Fetches data using Reddit's API for technical support subreddits.  (TODO: .py, functional as .ipynb)
└──  modeling
      ├── predict.py <- Makes multi-class classification prediction on which Subreddit to post in.  (TODO)
      └── train_model.py <- Trains our model for use in predict.py  (TODO)