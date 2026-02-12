# 🚌 Stockholm Transport Tracker (Level 1: Student)

A simple ETL script to collect real-time bus movement data in Stockholm.

## 📝 Description
The script connects to the Trafiklab API (SL Departures 4), downloads bus arrival data for a specific stop, cleans it, and saves it to a local DuckDB database.

**Key Features:**
* 🔄 **Extract:** Polls the API once every minute.
* 🧹 **Transform:** JSON cleaning, type conversion, delay calculation.
* 💾 **Load:** Saves to DuckDB (Append-only).
* 🛡 **Safety:** Network and API error handling, crash protection.

## 🛠 Tech Stack
* **Language:** Python 3.10+
* **Package Manager:** uv
* **Database:** DuckDB
* **Libraries:** pandas, requests, sqlalchemy, python-dotenv

## 🚀 Installation & Usage

1. **Navigate to the folder:**
    ```bash
    cd 01-student/01-transport-tracker
    ```

2. **Install dependencies (via uv):**
    ```bash
    uv sync
    ```

3. **Environment Setup: Create a .env file and add your API key:**

    ```Ini, TOML
    TRAFIKLAB_API_KEY=your_api_key_here
    SITE_ID=9117
    # Add other config variables if necessary
    ```

4. **Run:**

    ```bash
    uv run python src/fetch_data.py
    ```

# 📊 Result
Data is saved to the bus_delays.duckdb file in the project root.