from sqlalchemy import create_engine, text
from sqlalchemy.engine import URL
from sqlalchemy.exc import SQLAlchemyError
import pandas as pd
from config_loader import load_config

# Database configuration
config = load_config()
dbConfig = config["DATABASE"]
SERVER = dbConfig.get("SERVER")
PORT = dbConfig.get("PORT")
DATABASE = dbConfig.get("DATABASE")
USERNAME = dbConfig.get("USERNAME")
PASSWORD = dbConfig.get("PASSWORD")
print(f"Connecting to {SERVER}:{PORT}/{DATABASE} as {USERNAME}")

connection_url = URL.create(
    drivername="mssql+pyodbc",
    username=USERNAME,
    password=PASSWORD,
    host=SERVER,
    port=PORT,
    database=DATABASE,
    query={
        "driver": "ODBC Driver 17 for SQL Server",
        "TrustServerCertificate": "yes",
        "timeout": "300",
        "Encrypt": "yes",
    },
)

def get_engine():
    try:
        engine = create_engine(
            connection_url,
            pool_pre_ping=True,
        )
        return engine
    except SQLAlchemyError as e:
        print(f"Error creating engine: {e}")
        return None
