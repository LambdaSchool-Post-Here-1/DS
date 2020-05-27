import os
import sqlite3
from sklearn.linear_model import LogisticRegression
from basilica import Connection
from dotenv import load_dotenv

load_dotenv()

# Load in basilica api key from .env
API_KEY = os.getenv("BASILICA_API_KEY", default='YOU SHALL NOT PASS!')

# Filepath for database
DATABASE_URI = os.path.join(os.path.dirname(__file__), "test_db.sqlite3")

def train_model():
    # Connect to basilica for embedding text
    basilica_connection = Connection(API_KEY)

    # Connect to database and create cursor
    sqlite_connection = sqlite3.connect(DATABASE_URI)
    sqlite_connection.row_factory = sqlite3.Row
    sqlite_cursor = sqlite_connection.cursor()

    # SQL commands to select all and delete null
    select_data = """
                SELECT 
                    *
                FROM
                    "test_db.sqlite3";
                """

    # print(data)

    # Execute select all commands
    data = sqlite_cursor.execute(select_data).fetchall()
    # Ensure the select command is working
    # for row in data:
    #     print(f"\nSubreddits: {row['subreddit']}")
    #     print(f"\nTest: {row['Text']}")

    print("TRAINING THE MODEL...")

    subreddits = []
    text_embeddings = []
    for row in data:
        subreddits.append(row['subreddit'])
        embedding = basilica_connection.embed_sentence(row['Text'], model="reddit")
        text_embeddings.append(embedding)
        

    # breakpoint()
    # print(subreddits, text_embeddings)

    classifier = LogisticRegression()
    classifier.fit(text_embeddings, subreddits)

    return classifier