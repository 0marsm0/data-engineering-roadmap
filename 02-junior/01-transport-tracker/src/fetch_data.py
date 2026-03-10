from config import TRAFIKLAB_API, DATABASE_URL, SITE_IDS, BASE_URL
import pandas as pd
from sqlalchemy import create_engine
import requests
import time
import logging
import sys

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[logging.StreamHandler(sys.stdout)],
)
logger = logging.getLogger(__name__)


def extract_data(url, site_id, api_key):
    try:
        response = requests.get(f"{url}{site_id}", params={"key": api_key}, timeout=10)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        logger.error(f"API Error: {e}")
        return None


def transform_data(raw):

    if not raw or "departures" not in raw:
        logger.warning("No departures data found in response.")
        return None

    data = raw["departures"]
    df = pd.json_normalize(data, sep="_")

    cols = {
        "trip_trip_id": "trip_id",
        "route_transport_mode": "transport_mode",
        "route_designation": "line_number",
        "route_name": "line",
        "route_direction": "direction",
        "route_origin_name": "start_station",
        "route_destination_name": "end_station",
        "stop_name": "stop_point_name",
        "scheduled": "scheduled_time",
        "realtime": "actual_time",
        "delay": "delay_seconds",
        "canceled": "is_canceled",
        "is_realtime": "is_realtime",
    }

    try:
        clean_df = df[list(cols.keys())].rename(columns=cols).copy()

        for col in ["scheduled_time", "actual_time"]:
            clean_df[col] = pd.to_datetime(clean_df[col], errors="coerce")

        clean_df["captured_at"] = pd.Timestamp.now()
        return clean_df
    except KeyError as e:
        logger.error(f"Transform error: Missing column {e}")
        return None


def load_data(df, table, db_con):
    try:
        df.to_sql(name=table, con=db_con, if_exists="append", index=False)
        logger.info(f"✅ Success: {len(df)} rows loaded to {table}")
    except Exception as e:
        logger.error(f"Database error: {e}")


if __name__ == "__main__":

    engine = create_engine(DATABASE_URL)

    connected = False
    logger.info("Starting service. Waiting for database...")

    for i in range(10):
        try:
            with engine.connect() as conn:
                logger.info("Database connection successful!")
                connected = True
                break
        except Exception as e:
            logger.warning(
                f"Attempt {i+1}/10: Database not ready yet. Retrying in 5s..."
            )
            time.sleep(5)

    if not connected:
        logger.critical("Could not connect to database after 10 attempts. Exiting.")
        sys.exit(1)

    while True:
        for site_id in SITE_IDS:
            try:
                raw_data = extract_data(BASE_URL, site_id, TRAFIKLAB_API)
                if raw_data:
                    filtered_data = transform_data(raw_data)
                    if filtered_data is not None:
                        load_data(filtered_data, "bus_delays", engine)
                    time.sleep(2)
                else:
                    logger.warning("No data received from API. Skipping cycle.")
            except Exception as e:
                logger.error(f"Unexpected error in main loop: {e}")

        time.sleep(60)
