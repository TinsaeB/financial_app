# financial_app/main.py
import uvicorn
from fastapi import FastAPI
from backend.purchasing.api import app as purchasing_app
from backend.sales.api import app as sales_app
from backend.warehouses.api import app as warehouses_app
from backend.treasury.api import app as treasury_app
from backend.budgeting.api import app as budgeting_app
from backend.ledger.api import app as ledger_app
from financial_advisor.api import app as financial_advisor_app

app = FastAPI()

app.include_router(purchasing_app, prefix="/purchasing", tags=["purchasing"])
app.include_router(sales_app, prefix="/sales", tags=["sales"])
app.include_router(warehouses_app, prefix="/warehouses", tags=["warehouses"])
app.include_router(treasury_app, prefix="/treasury", tags=["treasury"])
app.include_router(budgeting_app, prefix="/budgeting", tags=["budgeting"])
app.include_router(ledger_app, prefix="/ledger", tags=["ledger"])
app.include_router(financial_advisor_app, prefix="/financial_advisor", tags=["financial_advisor"])

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)