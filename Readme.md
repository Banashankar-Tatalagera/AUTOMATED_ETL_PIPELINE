# Automated ETL Pipeline

An end-to-end crypto market data pipeline built with Python, FastAPI, PostgreSQL, Pandas, Streamlit, and Docker. The project ingests market data from a public crypto API, validates and transforms it, loads it into PostgreSQL, exposes the data through a FastAPI backend, and visualizes the result in a Streamlit dashboard.

## Overview

The application is organized around three layers:

1. Extraction: fetch raw market data from the external API.
2. Transformation: clean the dataset and derive analytics-friendly features.
3. Load and Serve: persist the data to PostgreSQL and serve it through FastAPI and Streamlit.

## Architecture

```mermaid
flowchart LR
		A[Public Crypto API] --> B[Extraction Client]
		B --> C[Response Validator]
		C --> D[DataFrame Parser]
		D --> E[Cleaner]
		E --> F[Feature Engineering]
		F --> G[PostgreSQL Loader]
		G --> H[(PostgreSQL)]
		H --> I[FastAPI /coins endpoints]
		I --> J[Streamlit Dashboard]

		K[Health Check] --> I
```

### Component Responsibilities

- `app/extract/`: calls the remote crypto market API, validates the response, and converts the payload to a Pandas DataFrame.
- `app/transform/`: removes duplicates, fills missing values, converts timestamps, and derives market-cap and trend features.
- `app/load/`: upserts transformed rows into PostgreSQL.
- `app/api/`: exposes REST endpoints for health checks and coin queries.
- `app/dashboard/`: renders the Streamlit UI, charts, metrics, and filters by consuming the API.
- `app/database/`: defines the SQLAlchemy engine, session, and `crypto_prices` table model.
- `app/logger.py`: writes runtime logs to `logs/pipeline.log`.

## How It Works

### ETL Flow

```mermaid
sequenceDiagram
		participant S as Scheduler/User
		participant E as Extraction Pipeline
		participant T as Transformation Pipeline
		participant L as Load Layer
		participant DB as PostgreSQL

		S->>E: run_pipeline()
		E->>E: fetch_data()
		E->>E: validate_response()
		E->>E: parse_to_dataframe()
		E-->>T: extracted DataFrame
		T->>T: clean_dataframe()
		T->>T: engineer_features()
		T-->>L: transformed DataFrame
		L->>DB: insert or update rows
```

### API Flow

The FastAPI app starts in `app/api/main.py`, creates tables on startup, and registers:

- `/health` for service status
- `/coins` for data retrieval and filtering

### Dashboard Flow

The Streamlit app in `app/dashboard/dashboard.py` fetches data from the API, applies sidebar filters, and renders:

- summary metrics
- Plotly charts
- detailed coin cards
- a data table

## Project Structure

```text
Readme.md
requirements.txt
Dockerfile
Dockerfile.streamlit
docker-compose.yml
app/
	api/
		main.py
		routes/
			coins.py
			health.py
		schemas.py
		dependencies.py
	dashboard/
		dashboard.py
		api_client.py
		charts.py
		details.py
		metrics.py
		sidebar.py
		table.py
	database/
		connection.py
		schema.py
	extract/
		client.py
		validator.py
		parser.py
		pipeline.py
	transform/
		cleaner.py
		engineer.py
		pipeline.py
	load/
		loader.py
		pipeline.py
data/
	raw/
	processed/
logs/
tests/
	database/
	dashboard/
	extraction/
	load/
	transformation/
```

## Tech Stack

- Python 3.11
- FastAPI for the backend API
- PostgreSQL for storage
- SQLAlchemy for ORM and session management
- Pandas for transformation
- Requests for external API calls
- Streamlit for the dashboard
- Plotly for visualizations
- Docker and Docker Compose for containerized execution

## Local Setup

### 1. Create and activate a virtual environment

```bash
python -m venv venv
venv\Scripts\activate
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Create a `.env` file

The project reads configuration from environment variables. A practical local `.env` looks like this:

```env
DATABASE_URL=postgresql://postgres:postgres@localhost:5432/etl_dashboard
API_BASE_URL=https://api.coingecko.com/api/v3
VS_CURRENCY=usd
PER_PAGE=100
PAGE=1
```

Optional legacy-style PostgreSQL variables are also present in `app/config.py`:

```env
DB_HOST=localhost
DB_PORT=5432
DB_NAME=etl_dashboard
DB_USER=postgres
DB_PASSWORD=postgres
```

## Running Locally

### 1. Start PostgreSQL

You can run PostgreSQL directly or use Docker Compose, then ensure `DATABASE_URL` points to the running database.

### 2. Run the ETL pipeline

```bash
python app/pipeline.py
```

This executes extraction, transformation, and load in sequence.

### 3. Start the API

```bash
uvicorn app.api.main:app --host 0.0.0.0 --port 8000
```

### 4. Start the dashboard

```bash
streamlit run app/dashboard/dashboard.py --server.address=0.0.0.0 --server.port=8501
```

## Docker Setup

The repository includes a Docker Compose stack with three services:

- `postgres` on port `5432`
- `api` on port `7000` mapped to container port `8000`
- `dashboard` on port `8501`

### Build and run

```bash
docker compose up --build
```

### Service URLs

- API: `http://localhost:7000`
- Dashboard: `http://localhost:8501`

## Environment Variables

| Variable | Purpose |
| --- | --- |
| `DATABASE_URL` | SQLAlchemy connection string used by the API and loader |
| `API_BASE_URL` | External crypto data API root |
| `VS_CURRENCY` | Quote currency for the market data request |
| `PER_PAGE` | Number of coins to request per page |
| `PAGE` | API page number |
| `DB_HOST` | Optional database host reference |
| `DB_PORT` | Optional database port reference |
| `DB_NAME` | Optional database name reference |
| `DB_USER` | Optional database user reference |
| `DB_PASSWORD` | Optional database password reference |
| `API_URL` | Dashboard API base URL, defaults to `http://api:8000` inside Docker |

## Data Model

The main table is `crypto_prices` defined in `app/database/schema.py`.

Important fields include:

- identity: `coin_id`, `symbol`, `name`
- price and volume: `current_price`, `market_cap`, `total_volume`
- market behavior: `price_change_percentage_24h`, `price_trend`
- derived fields: `date`, `time`, `hour`, `weekday`, `market_cap_category`
- audit field: `loaded_at`

## API Endpoints

### Health

- `GET /health` - returns service health status

### Coins

- `GET /coins` - paginated list of coins with optional sorting
- `GET /coins/top10` - top 10 coins by market cap
- `GET /coins/bullish` - coins where `price_trend` is Bullish
- `GET /coins/bearish` - coins where `price_trend` is Bearish
- `GET /coins/search?name=bitcoin` - case-insensitive name search
- `GET /coins/category/{category}` - filter by market-cap category
- `GET /coins/{coin_id}` - fetch one coin by `coin_id`

### Query Parameters for `GET /coins`

- `limit`: number of rows to return, default `20`, max `100`
- `offset`: offset into the result set, default `0`
- `sort_by`: one of `coin_id`, `name`, `current_price`, `market_cap`, `market_cap_rank`, `total_volume`, `last_updated`
- `order`: `asc` or `desc`

## Validation and Tests

The repository currently includes script-style validation files under `tests/` rather than a single unified test runner.

Examples of available checks:

- `tests/test_config.py`
- `tests/database/test_connection.py`
- `tests/database/test_schema.py`
- `tests/extraction/test_client.py`
- `tests/extraction/test_parser.py`
- `tests/extraction/test_validator.py`
- `tests/extraction/test_pipeline.py`
- `tests/load/test_loader.py`
- `tests/transformation/test_cleaner.py`
- `tests/transformation/test_engineer.py`
- `tests/transformation/test_transform_pipeline.py`
- `tests/dashboard/test_api_client.py`

Run individual scripts with Python if you want a quick smoke check, for example:

```bash
python tests/extraction/test_client.py
python tests/dashboard/test_api_client.py
```

## Logging

Runtime logs are written to `logs/pipeline.log`. The logger is configured in `app/logger.py` to log both to the file and to the console.

## Notes

- `app/db_test.py` imports `config` directly, so it is safest to run it from the `app/` directory or adjust `PYTHONPATH` accordingly.
- `app/api/main.py` creates database tables on startup via SQLAlchemy metadata.
- `app/api/routes/coins.py` currently exposes several useful query patterns for downstream analytics and dashboard filtering.

## Future Work

- Add a proper automated test runner entrypoint.
- Add a scheduler or cron-based job to run `app/pipeline.py` on a fixed interval.
- Add retry and backoff handling for the upstream crypto API.
- Add migration tooling such as Alembic for schema evolution.


