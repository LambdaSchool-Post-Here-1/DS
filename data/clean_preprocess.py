""""Cleans data for usage with our NLP model."""

import pandas as pd
import re
import spacy
from spacy.tokenizer import Tokenizer
import string

nlp = spacy.load('en_core_web_lg')
tokenizer = Tokenizer(nlp.vocab)

# Extending stop words relative to our use case.
STOP_WORDS = nlp.Defaults.stop_words.union(["doesnt", "wont", "cant"])

def clean_data(clean=True, tokenize=True):
    """Default cleaning function for cleaning data fetched by fetch_data.py
       Cleans & Tokenizes our Text."""

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

    tokens = []  # Empty list to populate with our tokens.

    for doc in tokenizer.pipe(dataframe['Text'].astype('unicode')):

        doc_tokens = []

        for token in doc:
            if ((token.text.lower() not in STOP_WORDS) &
            (token.is_punct==False)):
                doc_tokens.append(token.text.lower())
        tokens.append(doc_tokens)

    df['Tokens'] = tokens

    df = df.drop(columns='Text')
    df.to_csv('datasets/cleaned_data.csv', index=False)



def tokenize(text_to_tokenize):
    """Tokenizes text"""
    punct = string.punctuation
    tokens = []  # Empty list to populate with our tokens.
    list_of_tokens = text_to_tokenize.split()
    for token in list_of_tokens:
        if (token.lower() not in STOP_WORDS) & (token not in punct):
            tokens.append(token)
    return tokens
