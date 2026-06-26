# Automated ETL Pipeline

This project is currently under development. It provides the base structure for a Python ETL pipeline with PostgreSQL connectivity, logging, and supporting project folders.



## Current Scope

- PostgreSQL configuration through environment variables
- Application logging to `logs/pipeline.log`
- Basic database connection check
- Simple smoke test for logging

## Project Structure

```text
Readme.md
requirements.txt
app/
	config.py
	db_test.py
	logger.py
data/
	raw/
	processed/
database/
docker/
docs/
logs/
tests/
	test_pipeline.py
```

## Setup

1. Create a virtual environment and activate it.

	 ```bash
	 python -m venv venv
	 venv\Scripts\activate
	 ```

2. Install the dependencies.

	 ```bash
	 pip install -r requirements.txt
	 ```

3. Create a `.env` file in the project root.

	 ```env
	 DB_HOST=localhost
	 DB_PORT=5432
	 DB_NAME=your_database
	 DB_USER=your_username
	 DB_PASSWORD=your_password
	 ```

## Configuration

The application reads the following environment variables:

- `DB_HOST`
- `DB_PORT`
- `DB_NAME`
- `DB_USER`
- `DB_PASSWORD`

`app/config.py` uses these values to build the PostgreSQL connection string.

## Running The Available Checks

To test the database connection, run:

```bash
cd app
python db_test.py
```

To run the logging smoke test, use:

```bash
python tests/test_pipeline.py
```

## Notes

- The pipeline logic is still being built.
- Some scripts are intended for local validation only.
- Logs are written to `logs/pipeline.log`.

-----------


