from config import TRAFIKLAB_API, DATABASE_URL, SITE_ID, BASE_URL
import pandas as pd
from sqlalchemy import create_engine
import requests


def extract_data(url, site_id, api_key):
    try:
        response = requests.get(f"{url}{site_id}", params={"key": api_key})
        response.raise_for_status()
        return response.json()
    except Exception as e:
        print(f"Error: {e}")


def transform_data(raw):

    data = raw["departures"]
    df = pd.json_normalize(data, sep="_")
    clean_df = df[
        [
            "route_designation",
            "stop_name",
            "scheduled",
            "realtime",
            "delay",
            "stop_lat",
            "stop_lon",
        ]
    ].copy()
    clean_df = clean_df.rename(
        columns={
            "stop_name": "stop_point_name",
            "scheduled": "scheduled_time",
            "realtime": "actual_time",
            "delay": "delay_seconds",
        }
    )

    clean_df[["scheduled_time", "realtime"]] = clean_df[
        ["scheduled_time", "realtime"]
    ].apply(pd.to_datetime)

    return clean_df


def load_data(cleaned_data, db_conn):
    pass


if __name__ == "__main__":

    # engine = create_engine(DATABASE_URL)
    print("Connecting to API")
    raw_data = extract_data(BASE_URL, SITE_ID, TRAFIKLAB_API)

    if raw_data == None:
        print("Exiting")
        exit()

    filtered_data = transform_data(raw_data)
    print(filtered_data)
    # load_data(filtered_data, engine)
