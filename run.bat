@echo off
cd financial_app
set PYTHONPATH=%cd%

:: Install dependencies
venv\Scripts\pip install -r requirements.txt

:: Start Redis server (ensure redis-server is running in WSL2)
::call redis-server

:: Start Celery worker
call venv\Scripts\celery -A backend.processing.tasks worker -l info


:: Run the FastAPI application
call venv\Scripts\uvicorn main:app --reload

:: Run the Streamlit application
call venv\Scripts\streamlit run frontend\app.py
