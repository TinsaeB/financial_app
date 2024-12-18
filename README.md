# SME Financial Management Web Application

## Project Overview
This project aims to develop a robust, scalable, and user-friendly financial management web application tailored for Small and Medium Enterprises (SMEs). The application leverages a microservices architecture with a Python backend (FastAPI, Django), a Streamlit frontend, and integrates a local Large Language Model (LLM) via Ollama for advanced financial advisory capabilities.

## Tech Stack

- **Backend Framework:**
    - FastAPI: For building high-performance, RESTful APIs for each microservice.
    - Django ORM: For defining and managing the database models within each microservice.
    - Django Admin: For providing a quick way to manage data through a user-friendly interface during development and initial data setup.
- **Frontend Framework:**
    - Streamlit: For creating a dynamic and interactive user interface.
- **Database:**
    - SQLite: For local data storage.
- **Data Visualization:**
    - Plotly: For generating interactive and visually appealing charts, graphs, and dashboards.
    - Pandas: For data manipulation, analysis, and pre-processing before visualization.
- **LLM Integration:**
    - Ollama: For running a local Large Language Model (LLM) to power the Financial Advisor module.
- **Messaging and Queueing System**
    - Redis and Celery: Redis will serve as the message broker, while Celery will manage the distribution and execution of asynchronous tasks.

## Architecture

The application is structured as a collection of independent microservices, each responsible for a specific business function. This modular design enhances maintainability, scalability, and fault isolation.

### Microservices Breakdown:
1.  **Purchasing Module:** Manages all aspects of the procurement process.
2.  **Sales Module:** Handles all sales-related activities.
3.  **Warehouses Module:** Manages inventory across different warehouses.
4.  **Treasury Module:** Manages the company's assets.
5.  **Processing Module:** Handles background processing tasks, such as generating reports, sending notifications, or performing periodic data updates.
6.  **Budgeting Module:** Allows for the creation and management of budgets.
7.  **Ledger Module:** Maintains the general ledger, recording all financial transactions.
8.  **Financial Advisor Module:** Provides intelligent financial insights and recommendations powered by a local LLM (Ollama).

### Core Database Service:
- Provides a centralized set of utility functions for common database operations, abstracting away the underlying database implementation.

## Implementation Details
- Each microservice has its own `api.py` file defining the FastAPI application and endpoints.
- Use Pydantic models (defined in `schemas.py`) for request and response validation.
- Each microservice has its own `models.py` file defining the database models using Django ORM.
- The `core_db/db_utils.py` file contains functions for interacting with the database.
- Asynchronous tasks are implemented using Redis and Celery.
- The `frontend/app.py` file contains the main Streamlit application.
- The `financial_advisor/llm_utils.py` file contains functions for interacting with Ollama.

## Installation and Setup
1.  Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
2.  Install Redis:
    ```bash
    sudo apt-get install redis-server
    ```
3.  Install Celery and Redis Python libraries:
    ```bash
    pip install celery redis
    ```
4.  Start Redis server
    ```bash
    redis-server
    ```
5.  Start Celery worker
    ```bash
    celery -A processing worker -l info
    ```
6.  Run the FastAPI application:
    ```bash
    uvicorn main:app --reload
    ```
7.  Run the Streamlit application:
    ```bash
    streamlit run frontend/app.py
    ```

## API Documentation
- Use FastAPI's automatic API documentation feature (available at /docs and /redoc endpoints).

## Code Comments
- Add clear and concise comments throughout the codebase to explain complex logic, algorithms, or design choices.
- Use docstrings to document functions, classes, and modules.

## Contribution Guidelines
- Follow the project's coding standards and best practices.
- Create a new branch for each feature or bug fix.
- Submit a pull request with a clear description of the changes.
#   f i n a n c i a l _ a p p 
 
 
