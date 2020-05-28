"""Training functions for our NLP model."""


import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import GridSearchCV, train_test_split
from sklearn.pipeline import Pipeline
import warnings

df = pd.read_csv('../data/datasets/cleaned_data.csv')


def model():
    """Tunes our hyperparameters to update model for new data fetches as
       trends change in devices and such, builds model based upon training,
       fits it, and returns the model."""

    # 70/30 Train-Test Split
    train, test = train_test_split(df, train_size=0.7, random_state=42)

    # n_splits warning, fix
    warnings.simplefilter("ignore", UserWarning)

    X_train = train['Tokens']
    y_train = train['Subreddit']

    X_test = test['Tokens']
    y_test = test['Subreddit']

    vect = TfidfVectorizer()
    rfc = RandomForestClassifier()

    pipe = Pipeline([('vect', vect), ('clf', rfc)])

    # Let's tune the parameters. At the end, we'll send out our parameters.

    # Run 1 - Tune our Vectorizer
    parameters = {
                  'vect__analyzer': ['word', 'char', 'char_wb'],
                  'vect__ngram_range': [(1, 1), (1, 2), (1, 3),
                                        (1, 4), (1, 5), (1, 6)],
                  'vect__norm': ['l1', 'l2']
                  }

    search = GridSearchCV(pipe, parameters, cv=5, n_jobs=-1, verbose=False)
    results = search.fit(X_train, y_train)

    # Best parameters from this run.
    vect__ngram_range = results.best_params_['vect__ngram_range']
    vect__analyzer = results.best_params_['vect__analyzer']
    vect__norm = results.best_params_['vect__norm']

    # Run 2 - Tune Classification model
    parameters = {
                  'vect__analyzer': [vect__analyzer],
                  'vect__ngram_range': [vect__ngram_range],
                  'vect__norm': [vect__norm],
                  'clf__class_weight': ['balanced', 'balanced_subsample'],
                  'clf__max_features': [None, 'sqrt', 'log2', 25, 50],
                  'clf__n_estimators': [25, 50, 100, 125, 150, 175, 200],
                  'clf__oob_score': [True, False]
                 }

    search = GridSearchCV(pipe, parameters, cv=5, n_jobs=-1, verbose=False)
    results = search.fit(X_train, y_train)

    params = results.best_params_

    # Now that we've tuned parameters, let's go ahead and build our model!
    vect = TfidfVectorizer(analyzer=params['vect__analyzer'],
                           ngram_range=params['vect__ngram_range'],
                           norm=params['vect__norm'])

    rfc = RandomForestClassifier(class_weight=params['clf__class_weight'],
                                 max_features=params['clf__max_features'],
                                 n_estimators=params['clf__n_estimators'],
                                 oob_score=params['clf__oob_score'])

    model = Pipeline([('vect', vect), ('clf', rfc)])
    model.fit(df['Tokens'], df['Subreddit'])

    return model
