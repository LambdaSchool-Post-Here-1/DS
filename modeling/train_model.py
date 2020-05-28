"""Training functions for our NLP model."""


import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import GridSearchCV, train_test_split
from sklearn.pipeline import Pipeline
import warnings

df = pd.read_csv('../data/datasets/cleaned_data.csv')


class model():
    """`tune_parameters` - Tunes our parameters for new data fetches.
       `nlp_model` - Trains and returns model fit with our parameters"""

    def __init__(self, training_params, model):
        self.training_params = training_params
        self.model = model

    def tune_parameters(self):
        """Tunes our hyperparameters to update model for new data fetches as
           trends change in devices and such."""

        train, test = train_test_split(df, train_size=0.7)  # Train-Test Split.

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

        # Run 1.
        parameters = {
                      'vect__ngram_range': [(1, 1), (1, 2), (1, 3),
                                            (1, 4), (1, 5)],
                      'vect__analyzer': ['word', 'char', 'char_wb']
                      }

        search = GridSearchCV(pipe, parameters, cv=5, n_jobs=-1, verbose=False)
        results = search.fit(X_train, y_train)

        # Best parameters from this run.
        vect__ngram_range = results.best_params_['vect__ngram_range']
        vect__analyzer = results.best_params_['vect__analyzer']

        # Run 2.
        parameters = {
                      'vect__ngram_range': [vect__ngram_range],
                      'vect__analyzer': [vect__analyzer],
                      'clf__n_estimators': [25, 50, 100, 125, 150, 175, 200],
                      'clf__max_features': [None, 'sqrt', 'log2'],
                      'clf__max_samples': [None, 25, 35, 50, 65, 70],
                      'clf__class_weight': ['balanced', 'balanced_subsample']
                     }

        search = GridSearchCV(pipe, parameters, cv=5, n_jobs=-1, verbose=False)
        results = search.fit(X_train, y_train)

        clf__n_estimators = results.best_params_['clf__n_estimators']
        clf__max_features = results.best_params_['clf__max_features']
        clf__max_samples = results.best_params_['clf__max_samples']

        # Run 3.
        parameters = {
                      'vect__analyzer': [vect__analyzer],
                      'vect__ngram_range': [vect__ngram_range],
                      'clf__n_estimators': [clf__n_estimators],
                      'clf__max_features': [clf__max_features],
                      'clf__class_weight': ['balanced', 'balanced_subsample'],
                      'clf__oob_score': [True, False]
                      }

        search = GridSearchCV(pipe, parameters, cv=5, n_jobs=-1, verbose=False)
        results = search.fit(X_train, y_train)

        training_params.self = results.best_params_
        return training_params

    def nlp_model(self, training_params):
        """Trains model for use in making predictions on user input"""

        params = training_params.self
        vect = TfidfVectorizer(analyzer=params['vect__analyzer'],
                               ngram_range=params['vect__ngram_range'])

        rfc = RandomForestClassifier(n_estimators=params['clf__n_estimators'],
                                     max_features=params['clf__max_features'],
                                     class_weight=params['clf__class_weight'],
                                     oob_score=params['clf__oob_score'])

        model = Pipeline([('vect', vect), ('clf', rfc)])
        model.fit(df['Tokens'], df['Subreddit'])

        return model
