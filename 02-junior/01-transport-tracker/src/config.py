import os
from dotenv import load_dotenv

load_dotenv(override=False)

TRAFIKLAB_API = os.getenv("TRAFIKLAB_API_KEY")
SITE_IDS = os.getenv("SITE_IDS").split(",")
SITE_IDS = [SITE_ID.strip() for SITE_ID in SITE_IDS]

BASE_URL = "https://realtime-api.trafiklab.se/v1/departures/"

DATABASE_URL = os.getenv("DATABASE_URL")

print(SITE_IDS)

print(f"CONFIG: Connecting to database: {DATABASE_URL}")

if not TRAFIKLAB_API:
    raise ValueError("TRAFIKLAB_API_KEY not found! Check your .env file")

if not DATABASE_URL:
    raise ValueError(
        "DATABASE_URL not set. In Docker check docker-compose.yml, locally check .env"
    )
