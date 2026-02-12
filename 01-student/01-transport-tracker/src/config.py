import os
from dotenv import load_dotenv

load_dotenv()

TRAFIKLAB_API = os.getenv("TRAFIKLAB_API_KEY")
SITE_ID = "740009117"
BASE_URL = "https://realtime-api.trafiklab.se/v1/departures/"

POSTGRES_HOST = os.getenv("POSTGRES_HOST")
POSTGRES_PORT = os.getenv("POSTGRES_PORT")
POSTGRES_DB = os.getenv("POSTGRES_DB")
POSTGRES_USER = os.getenv("POSTGRES_USER")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")

config_dict = {
    "TRAFIKLAB_API": TRAFIKLAB_API,
    "POSTGRES_HOST": POSTGRES_HOST,
    "POSTGRES_PORT": POSTGRES_PORT,
    "POSTGRES_DB": POSTGRES_DB,
    "POSTGRES_USER": POSTGRES_USER,
    "POSTGRES_PASSWORD": POSTGRES_PASSWORD,
}

for key, el in config_dict.items():
    if el is None:
        raise ValueError(f"Error: {key} not found! Check your .env")


DB_PATH = os.getenv("DB_PATH")

# DATABASE_URL = f"duckdb+psycopg2://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"
DATABASE_URL = f"duckdb:///{DB_PATH}"
