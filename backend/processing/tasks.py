from .celery import app
from time import sleep

@app.task
def generate_monthly_financial_report():
    # Simulate a long-running task
    print("Starting report generation...")
    sleep(30)
    print("Report generated!")
    # Here you would actually generate the report, potentially saving it to a database or file storage.
    return {"status": "success", "report_id": "123"}

@app.task
def send_low_stock_alert(product_name, warehouse_name):
    print(f"Low stock alert for {product_name} in {warehouse_name}!")
    # Here you would send an email or notification
    return {"status": "success", "message": f"Alert sent for {product_name}"}
