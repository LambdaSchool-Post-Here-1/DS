# DS
Data Science repository for Lambda School's PostHere build for classifying the proper technical support Subreddit a post should go in using a Natural Language Processing model. Our goal was to create a NLP model to classify the proper Subreddit a post should go into in under the span of a week. We worked cross-collaboratively with peers from other career tracks to complete this project.


[Model Deployed Here](https://marketing-page-mu.now.sh/)
## Directory Structure
```
├── README.md  <- You are here! Data Science README file.
├── requirements.txt  <- The requirements file for reproducing environment.-->TODO<--
├── data <- Data collection, cleaning, preprocessing, CSV files.
│    ├── datasets <- CSV files of Fetched / Cleaned Data
│    │    ├── cleaned_data.csv <- CSV output of clean_preprocess.py - cleans and Tokenizes text.
│    │    └── fetched_data.csv <- CSV output of fetch_data.py - raw fetched data.
│    ├── clean_preprocess.py <- Cleaning / tokenizing final data for usage in modeling.
│    └── fetch_data.py  <- Fetches data using Reddit's API for technical support subreddits.
├── modeling <- Directory containing files for training / prediction (our model)
│    ├── predict.py <- Makes multi-class classification prediction on which Subreddit to post in
│    └── train_model.py <- Trains our model for use in predict.py
├── notebooks
│    ├── data_exploration.ipynb <- Jupyter notebook for data exploration.
│    └── model_selection.ipynb <- Jupyter notebook for model selection.
└── data_engineering <- Directory to store data engineering progress
     ├── routes <- Create routes to important data pages
     │    ├── home_routes.py <- Create route to home page
     │    └── predict_routes.py <- Create route to predict page
     ├── models.py <- models for database, classes, helper methods, etc
     └── __init__.py <- init file...main file where app is created and run
```

## Challenges Faced this Build Week:

### Machine Learning Engineering:
Considering the list of Subreddits we were trying to classify, the model performs well. Two of the subreddits were extremely similar in nature:
- `/r/24hoursupport`
- `/r/techsupport`

Furthermore, there are a lot of topics that can be somewhat related, such as can potentially be seen in...
- `/r/buildapc`
- `/r/pcgamingtechsupport`

... such as in different computer components. For a project such as this in such a short time period, more than anything, I'd like to see survey results on how well the model classified the post to a subreddit that could be expected.

In an attempt to overcome this, I did some decent parameter tuning on several models for model selection. I ultimately ended up using a TF-IDF Vectorizer / Random Forest Classifier model, accompanied by a custom tokenization function, to build this model.

### Data Engineering:
The data engineering skeleton came together nicely and within a local environment the connection between the machhine learning model and the data engineering code flowed nicely, however in the deployment process a number of errors occurred with package issues. Overcoming this issue took significant time, research, and a sequential experimental approach that ultimately led to the end product.

Upon deployment we ran into a CORS policy issue that didn't allow the frontend/backend code to connect to my code. After doing some more research I was able to modify my code to allow access and get our program running as it should.

**Contributors:**

**Data Engineer** - Daniel Benson

**Machine Learning Engineer** - Kenneth T. Barrett
