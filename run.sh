#!/bin/bash

# Install dependencies
financial_app/venv/Scripts/pip install -r financial_app/requirements.txt

# Start Redis server
financial_app/venv/Scripts/python -m redis.server &

# Start Celery worker
financial_app/venv/Scripts/celery -A processing worker -l info &

# Run the FastAPI application
financial_app/venv/Scripts/uvicorn main:app --reload &

# Run the Streamlit application
financial_app/venv/Scripts/streamlit run frontend/app.py
