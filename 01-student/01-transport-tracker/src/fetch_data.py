from config import TRAFIKLAB_API, DATABASE_URL, SITE_ID, BASE_URL
import pandas as pd
from sqlalchemy import create_engine
import requests
import time


def extract_data(url, site_id, api_key):
    try:
        response = requests.get(f"{url}{site_id}", params={"key": api_key}, timeout=10)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        print(f"API Error: {e}")
        return None


def transform_data(raw):

    if not raw or "departures" not in raw:
        return None

    data = raw["departures"]
    df = pd.json_normalize(data, sep="_")

    cols = {
        "route_designation": "route_number",
        "stop_name": "stop_point_name",
        "scheduled": "scheduled_time",
        "realtime": "actual_time",
        "delay": "delay_seconds",
        "stop_lat": "stop_lat",
        "stop_lon": "stop_lon",
    }

    try:
        clean_df = df[list(cols.keys())].rename(columns=cols).copy()

        for col in ["scheduled_time", "actual_time"]:
            clean_df[col] = pd.to_datetime(clean_df[col], errors="coerce")

        clean_df["captured_at"] = pd.Timestamp.now()
        return clean_df
    except KeyError as e:
        print(f"Transform error: Missing column {e}")


def load_data(df, table, db_con):
    try:
        df.to_sql(name=table, con=db_con, if_exists="append", index=False)
        print(f"Success: {len(df)} rows loaded to {table}")
    except Exception as e:
        print(f"Database error: {e}")


if __name__ == "__main__":

    engine = create_engine(DATABASE_URL)
    print("Connecting to API")
    try:
        while True:
            try:
                raw_data = extract_data(BASE_URL, SITE_ID, TRAFIKLAB_API)

                if raw_data:
                    filtered_data = transform_data(raw_data)
                    if filtered_data is not None:
                        load_data(filtered_data, "bus_delays", engine)
                else:
                    print("No data received. Skipping ...")
            except Exception as e:
                print(f"Unexpected error: {e}")
            time.sleep(60)
    except KeyboardInterrupt:
        print("Stop initiated by user.")
    finally:
        engine.dispose()
        print("Database connection closed!")
