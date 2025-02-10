#!/bin/bash

# Install dependencies
./venv/Scripts/pip install -r requirements.txt

# Start Redis server
./venv/Scripts/python -m redis.server &

# Start Celery worker
./venv/Scripts/celery -A processing worker -l info &

# Run the FastAPI application
./venv/Scripts/uvicorn main:app --reload &

# Run the Streamlit application
./venv/Scripts/streamlit run frontend/app.py
