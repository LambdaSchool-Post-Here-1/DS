"""

Baseline training file used in app production

"""


import os
import sqlite3
import sklearn
from sklearn.linear_model import LogisticRegression
from basilica import Connection
import psycopg2


# Load in basilica api key
API_KEY = "d3c5e936-18b0-3aac-8a2c-bf95511eaaa5"

# Filepath for database
DATABASE_URL = "postgres://khqrpuidioocyy:28306f6ac214b8c5ff675ab1e38ed6007d0b810d0a538df3e0db3da0f3cde717@ec2-18-210-214-86.compute-1.amazonaws.com:5432/d1jb037n8m5r20"

# Heroku postgresql credentials
DB_NAME = "d1jb037n8m5r20"
DB_USER = "khqrpuidioocyy"
DB_PASSWORD = "28306f6ac214b8c5ff675ab1e38ed6007d0b810d0a538df3e0db3da0f3cde717"
DB_HOST = "ec2-18-210-214-86.compute-1.amazonaws.com"

# Connect to basilica for embedding text
basilica_connection = Connection(API_KEY)

sql_connection = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD, host=DB_HOST)
sql_cursor = sql_connection.cursor()


def train_model():
    

    # SQL commands to select all and delete null
    select_data = """
                SELECT 
                    *
                FROM
                    "postgresql-shallow-75985";
                """
    # breakpoint()
    # print(data)

    # Execute select all commands
    sql_cursor.execute(select_data)
    data = sql_cursor.fetchall()
    # Ensure the select command is working
    # for row in data:
    #     print(f"\nSubreddits: {row['subreddit']}")
    #     print(f"\nTest: {row['Text']}")

    print("TRAINING THE MODEL...")

    subreddits = []
    text_embeddings = []
    # breakpoint()
    for row in data:
        subreddits.append(row[1])
        embedding = basilica_connection.embed_sentence(row[2], model="reddit")
        text_embeddings.append(embedding)
        

    # breakpoint()
    # print(subreddits, text_embeddings)

    classifier = LogisticRegression()
    classifier.fit(text_embeddings, subreddits)

    return classifier

if __name__ == "__main__":
    classifier = train_model()
    # breakpoint()