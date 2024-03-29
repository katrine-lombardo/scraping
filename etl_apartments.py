import os
import psycopg2
import requests
import pandas as pd
import importlib.util
from sqlalchemy import create_engine
from dotenv import load_dotenv


load_dotenv()

host = os.getenv("PGHOST")
port = os.getenv("PGPORT")
user = os.getenv("PGUSER")
password = os.getenv("PGPASSWORD")
dbname = os.getenv("PGDATABASE")


engine = create_engine(f"postgresql://{user}:{password}@{host}:{port}/{dbname}")


def main(df):
    df.to_sql("unit_records", engine, if_exists="append", index=False)


if __name__ == "__main__":
    spec = importlib.util.spec_from_file_location(
        "apartment_prices_selenium", "apartment_prices_selenium.py"
    )
    apartment_prices_selenium = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(apartment_prices_selenium)

    df = apartment_prices_selenium.main()
    main(df)
