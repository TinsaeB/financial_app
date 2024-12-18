from fastapi import FastAPI
from .tasks import generate_monthly_financial_report, send_low_stock_alert

app = FastAPI()

@app.post("/generate-report")
async def trigger_report_generation():
    result = generate_monthly_financial_report.delay() # .delay() makes it asynchronous
    return {"task_id": result.id, "message": "Report generation initiated."}

@app.post("/send-alert")
async def trigger_low_stock_alert(product_name: str, warehouse_name: str):
    result = send_low_stock_alert.delay(product_name, warehouse_name)
    return {"task_id": result.id, "message": "Low stock alert initiated."}
