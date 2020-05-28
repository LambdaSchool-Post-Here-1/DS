"""Fetches top 100 posts from list of tech support subreddits."""


import os
import pandas as pd
import praw  # Reddit API wrapper
from decouple import config


def fetch(num_posts=250):
    """Fetches the top posts for our list of technical support subreddits.
       `num_posts` (Default = 250) # of posts to fetch from each subreddit."""

    # Make connection to Reddit API
    r = praw.Reddit(client_id=config('CLIENT_ID'),
                    client_secret=config('CLIENT_SECRET'),
                    username=config('USERNAME'),
                    password=config('PASSWORD'),
                    user_agent=config('USER_AGENT'))

    # Tech support subreddits that we'll be using.
    subreddits = ['24hoursupport', 'Android', 'Applehelp', 'asktechnology',
                  'buildapc', 'linux4noobs', 'pcgamingtechsupport',
                  'talesfromtechsupport', 'techsupport']

    # Making a dataframe with the columns we'll be using.
    df = pd.DataFrame(columns=['Subreddit', 'Text'])

    # Populates dataframe created above.

    # HOT
    for sr in subreddits:
        subreddit = r.subreddit(sr)
        for submission in subreddit.hot(limit=num_posts):
            post = r.submission(id=submission.id)
            if post.selftext != '':
                df = df.append({'Subreddit': subreddit.display_name,
                                'Text': post.selftext}, ignore_index=True)

    # TOP
    for sr in subreddits:
        subreddit = r.subreddit(sr)
        for submission in subreddit.top(limit=num_posts):
            post = r.submission(id=submission.id)
            if post.selftext != '':
                df = df.append({'Subreddit': subreddit.display_name,
                                'Text': post.selftext}, ignore_index=True)

    df = df.dropna()  # Drop any NaN values before sending to CSV.

    df.to_csv('datasets/fetched_data.csv', index=False)  # Sending to CSV
