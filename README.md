# SME Financial Management Application

This application provides a comprehensive financial management system for small and medium-sized enterprises (SMEs). It includes the following modules:

## Modules

-   **Budgeting**: Allows users to create and manage budgets, and analyze budget variances.
-   **Ledger**: Manages the general ledger, records transactions, and generates financial statements.
-   **Purchasing**: Handles supplier management, purchase orders, and payments.
-   **Sales**: Manages customer information, sales orders, and installment plans.
-   **Warehouses**: Manages inventory items and stock transfers.
-   **Treasury**: Tracks assets, loans, and repayment schedules.
-   **Financial Advisor**: Provides insights and recommendations based on financial reports.

## Implemented Features

### Phase 1: Backend Development

-   All backend microservices (budgeting, ledger, purchasing, sales, warehouses, treasury) are implemented with SQLAlchemy models and Pydantic schemas.
-   The Ledger module is fully functional, including endpoints for Income Statement, Balance Sheet, Cash Flow Statement, Aged Receivables, Aged Payables, Trial Balance, and General Ledger Detail.
-   The Purchasing and Sales modules handle Accounts Payable (AP) and Accounts Receivable (AR) functionalities, respectively.
-   The Asset Management, Cash Management, and Budgeting modules are implemented with basic functionalities.
-   All necessary database models are created and their relationships are defined.
-   Database interactions are centralized and consistent across all microservices using the `core_db/db_utils.py` file.
-   All core API endpoints are implemented with appropriate request and response schemas.
-   The required calculations for gross profit, net profit, revenue, expenses, and COGS are implemented.

### Phase 2: Frontend Development

-   A logical folder structure for Streamlit pages and components is designed in the `frontend` directory.
-   An interactive and informative financial dashboard is implemented, displaying key financial metrics, summaries, outstanding invoices, KPIs, and budget vs. actual performance.
-   Dedicated Streamlit pages are created for each module (Purchasing, Sales, Warehouses, Treasury, Budgeting, Ledger) with placeholders for forms, tables, filtering, sorting, and error handling.
-   API calls are implemented from the Streamlit frontend to interact with the backend microservices.
-   A function is implemented in the frontend to process JSON data from the API and display it in a user-friendly format, including the Income Statement, Balance Sheet, Cash Flow Statement, Aged Receivables, Aged Payables, Trial Balance, and General Ledger Detail reports.

### Phase 3: Integration, Testing, and Refinement

-   Basic end-to-end testing has been performed.
-   Database queries have been optimized by adding pagination.
-   Basic documentation has been added to the README.md file.

## Next Steps

-   Implement full end-to-end testing for all features.
-   Collect feedback from stakeholders and make necessary improvements to the application.
-   Document the APIs and microservices.
-   Add comments and docstrings to the code.

## API Documentation

The API endpoints for each microservice are defined in the respective `api.py` files within the `backend` directory.

## Microservices Documentation

Each microservice is located in its own directory within the `backend` directory. The models, schemas, and API endpoints for each microservice are defined in the `models.py`, `schemas.py`, and `api.py` files, respectively.

## Code Documentation

Comments and docstrings will be added to the code in the next steps.
