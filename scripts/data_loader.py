import os
from sqlalchemy import create_engine
import pandas as pd

from dotenv import load_dotenv
# Load environment variables from .env file
load_dotenv()  

def load_data_from_db(query):
    # Get PostgreSQL connection details from environment variables
    host = os.getenv("DB_HOST")
    port = os.getenv("DB_PORT")
    db = os.getenv("DB_NAME")
    user = os.getenv("DB_USER")
    password = os.getenv("DB_PASSWORD")

    print(f"Host: {host}, Port: {port}, DB: {db}, User: {user}")

    # Construct the connection string using the environment variables
    DATABASE_URL = f'postgresql://{user}:{password}@{host}:{port}/{db}'

    # Create database engine
    engine = create_engine(DATABASE_URL)

    # Load data into DataFrame
    df = pd.read_sql(query, engine)

    return df
