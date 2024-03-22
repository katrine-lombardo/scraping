import os
import psycopg2
import requests
import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv


load_dotenv()

host = os.getenv("PGHOST")
port = os.getenv("PGPORT")
user = os.getenv("PGUSER")
password = os.getenv("PGPASSWORD")
dbname = os.getenv("PGDATABASE")


engine = create_engine(f"postgresql://{user}:{password}@{host}:{port}/{dbname}")

df.to_sql("unit_records", engine, if_exists="append", index=True)
