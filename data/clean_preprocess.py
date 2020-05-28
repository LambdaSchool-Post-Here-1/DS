""""Cleans data for usage with our NLP model."""

import pandas as pd
import re
import spacy
import string
from en_core_web_sm_2_2_5 import en_core_web_sm

# spacy.load('en_core_web_md')
nlp = en_core_web_sm.load()

# Extending stop words relative to our use case.
STOP_WORDS = nlp.Defaults.stop_words.union(["doesnt", "wont", "cant", "got",
                                            "use", "im", "like", "know",
                                            "dont", "ive"])


def clean_data():
    """Default cleaning function for cleaning data fetched by fetch_data.py
       Cleans & Tokenizes our Text."""

    punct = string.punctuation
    df = pd.read_csv('datasets/fetched_data.csv')

    # Replace linebreaks with whitespace
    df['Text'] = df['Text'].str.replace('\n', ' ')
    df['Text'] = df['Text'].str.replace('*', '')  # Removes asterisks
    blank = ' [](/resolved)'  # Blank resolved post.
    df = df[df['Text'] != blank].reset_index(drop=True)  # Remove blank posts

    # Removes URLs
    url_regex = (r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]' +
                 r'|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')

    df['Text'] = df['Text'].apply(lambda x: re.sub(url_regex, '', x))

    # Removes anything in brackets (generally irrelevant)
    df['Text'] = df['Text'].apply(lambda x: re.sub(r'\[.*?\]', '', x))

    # Tokenizing
    tokens = []  # Empty list to populate with our tokens.

    for text in df['Text']:
        list_of_tokens = re.split(r'[/\s]', text)
        # Remove punctuation
        table = str.maketrans('', '', string.punctuation)
        list_of_tokens = [t.translate(table) for t in list_of_tokens]

        doc_tokens = []
        for token in list_of_tokens:
            if (token.lower() not in STOP_WORDS) & (token not in punct):
                doc_tokens.append(token.lower())
        tokens.append(doc_tokens)
    df['Tokens'] = tokens

    df = df.drop(columns='Text')  # Drop text column.
    df = df.dropna()  # Drop NaN values.

    df.to_csv('datasets/cleaned_data.csv', index=False)
    return


def tokenize(text_to_tokenize):
    """Tokenizes text for usage in predictions"""

    punct = string.punctuation
    tokens = []  # Empty list to populate with our tokens.
    list_of_tokens = text_to_tokenize.split()
    # Remove punctuation
    table = str.maketrans('', '', string.punctuation)
    list_of_tokens = [t.translate(table) for t in list_of_tokens]

    for token in list_of_tokens:
        if (token.lower() not in STOP_WORDS) & (token not in punct):
            tokens.append(token.lower())
    return tokens
