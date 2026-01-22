# 🚀 Data Engineering Roadmap: Student → Senior

![Python](https://img.shields.io/badge/Python-3.11+-blue?logo=python&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-Enabled-2496ED?logo=docker&logoColor=white)
![Airflow](https://img.shields.io/badge/Airflow-Orchestration-017CEE?logo=apacheairflow&logoColor=white)
![Kafka](https://img.shields.io/badge/Kafka-Streaming-231F20?logo=apachekafka&logoColor=white)
![Spark](https://img.shields.io/badge/Spark-Big_Data-E25A1C?logo=apachespark&logoColor=white)
![Postgres](https://img.shields.io/badge/PostgreSQL-DWH-4169E1?logo=postgresql&logoColor=white)
![dbt](https://img.shields.io/badge/dbt-Transformations-FF694B?logo=dbt&logoColor=white)
![Grafana](https://img.shields.io/badge/Grafana-Observability-F46800?logo=grafana&logoColor=white)
![Status](https://img.shields.io/badge/Status-Active_Development-green)

---

## 📌 About This Repository

This monorepo documents my **engineering evolution from Student to Middle+ Data Engineer**.

Instead of isolated demo projects, I progressively **upgrade the same 3 data platforms**:
from local Python scripts to automated, scalable, and near-real-time systems.

The focus is on **real-world data engineering problems**:
- unstable APIs
- growing data volumes
- idempotency & reproducibility
- batch → streaming transition
- storage & compute trade-offs

---

## 🎯 Target Roles

This repository is designed to demonstrate skills relevant for:
- **Data Engineer** (primary)
- **Data Analyst** (data modeling & SQL focus)
- **Cloud / Platform Engineer** (Docker, orchestration, infra mindset)

---

## 🗺️ How to Read This Repo

The repository is structured by **evolution phases**, not by tools:

- **[01-student](./01-student/)** — *The Fetcher*
  **Focus:** Python, SQL, data structures, local execution

- **[02-junior](./02-junior/)** — *The Automator*
  **Focus:** Docker, orchestration, reproducibility, data modeling

- **[03-middle](./03-middle/)** — *The Streamer*
  **Focus:** Kafka, Spark, scalable storage, real-time pipelines

Each phase upgrades the **same projects** with new constraints and tools.

---

## 🏗️ Core Projects Overview

| Project | Domain | What It Demonstrates |
|------|------|------|
| **Stockholm Metro Pulse** | 🌊 Streaming | Real-time ingestion, Kafka, monitoring |
| **GitHub Trends Analyzer** | 🏗️ Big Data | Batch processing, modeling, Spark & Data Lake |
| **Local HR Assistant** | 🧠 AI / RAG | Data products, vector search, privacy-first design |

> **Note:**
> The AI project is treated as a **data product and downstream consumer**
> of structured data — not as a core ML research system.

---

## 🌊 Project 1: Stockholm Metro Pulse (Streaming)

**Problem:**
Public transport APIs are unstable, noisy, and time-sensitive.
This project explores how real-time mobility data can be ingested, stored, and visualized reliably.

### 🎓 Student — *The Fetcher*
- Polls Trafiklab (SL) API every minute
- JSON → coordinates → PostgreSQL with timestamps
- Tools: `uv`, `requests`, `pandas`, `PostgreSQL`
- **Result:** Historical movement data accumulated in a relational database

### 🐣 Junior — *The Automator*
- Script runs continuously without manual intervention
- Dockerized ingestion
- Airflow DAG with logging & failure alerts (Telegram)
- Tools: `Docker Compose`, `Airflow`, `Python logging`
- **Result:** Autonomous, schedulable ingestion pipeline

### 🚀 Middle+ — *The Streamer*
- Transition from polling → streaming
- Producer publishes vehicle positions to Kafka
- Consumer aggregates data for visualization
- Grafana dashboard: *“Where is my bus right now?”*
- Tools: `Apache Kafka`, `Grafana` *(optional: Spark Streaming)*
- **Result:** Near real-time transport monitoring system

---

## 🏗️ Project 2: GitHub Trends Analyzer (Big Data)

**Problem:**
GitHub event archives are massive, semi-structured, and unsuitable for naive processing.

### 🎓 Student — *The Parser*
- Processes ~2–3 GB/day compressed JSON
- Streaming file read (no full memory load)
- Filters PushEvents, computes top repositories
- Tools: `gzip`, `json`, `pandas (chunks)`
- **Result:** Daily analytical CSV reports

### 🐣 Junior — *The Modeler*
- Monthly data loaded into analytical storage
- dbt models: `dim_users`, `dim_repos`, `fct_events`
- Star schema for BI & analytics
- Tools: `DuckDB / PostgreSQL`, `dbt core`, `SQL`
- **Result:** Clean analytical data warehouse

### 🚀 Middle+ — *The Scaler*
- Year-scale data (TBs)
- Spark cluster for distributed processing
- JSON → Parquet / Iceberg (Data Lake)
- Advanced analytics (sessionization)
- Tools: `PySpark`, `Dockerized Spark`, `Parquet`
- **Result:** Optimized Data Lake architecture

---

## 🧠 Project 3: Local HR Assistant (AI & Privacy)

**Problem:**
Recruiters often need semantic search over private documents without cloud exposure.

### 🎓 Student — *The Searcher*
- Local keyword-based resume search
- PDF text extraction
- Tools: `Python`, `pypdf`
- **Result:** CLI utility for basic document filtering

### 🐣 Junior — *The Vectorizer*
- Semantic search without keyword matching
- Local embeddings via Ollama
- Vector storage in LanceDB
- Tools: `Ollama`, `SentenceTransformers`, `LanceDB`
- **Result:** Context-aware resume search

### 🚀 Middle+ — *The Application*
- Streamlit UI
- Chat-based candidate summaries
- Fully containerized delivery
- Tools: `Streamlit`, `RAG pipeline`, `Docker`
- **Result:** Deployable, privacy-first AI data product
