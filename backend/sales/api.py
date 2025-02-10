from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from core_db.db_utils import get_db, create, query
from . import models, schemas

app = APIRouter()

# --- Customers ---

@app.post("/customers/", response_model=schemas.Customer)
def create_customer(customer: schemas.CustomerCreate, db: Session = Depends(get_db)):
    db_customer = models.Customer(**customer.dict())
    return create(db, db_customer)

@app.get("/customers/", response_model=List[schemas.Customer])
def get_customers(db: Session = Depends(get_db), skip: int = 0, limit: int = 100):
    return query(db, models.Customer, offset=skip, limit=limit)

@app.get("/customers/{customer_id}", response_model=schemas.Customer)
def get_customer(customer_id: int, db: Session = Depends(get_db)):
    db_customer = db.query(models.Customer).filter(models.Customer.id == customer_id).first()
    if not db_customer:
        raise HTTPException(status_code=404, detail="Customer not found")
    return db_customer

@app.put("/customers/{customer_id}", response_model=schemas.Customer)
def update_customer(customer_id: int, customer: schemas.CustomerCreate, db: Session = Depends(get_db)):
    db_customer = db.query(models.Customer).filter(models.Customer.id == customer_id).first()
    if not db_customer:
        raise HTTPException(status_code=404, detail="Customer not found")
    for key, value in customer.dict().items():
        setattr(db_customer, key, value)
    db.commit()
    db.refresh(db_customer)
    return db_customer

@app.delete("/customers/{customer_id}")
def delete_customer(customer_id: int, db: Session = Depends(get_db)):
    db_customer = db.query(models.Customer).filter(models.Customer.id == customer_id).first()
    if not db_customer:
        raise HTTPException(status_code=404, detail="Customer not found")
    db.delete(db_customer)
    db.commit()
    return {"message": "Customer deleted successfully"}

# --- Sales Orders ---

@app.post("/sales-orders/", response_model=schemas.SalesOrder)
def create_sales_order(sales_order: schemas.SalesOrderCreate, db: Session = Depends(get_db)):
    db_sales_order = models.SalesOrder(**sales_order.dict())
    return create(db, db_sales_order)

@app.get("/sales-orders/", response_model=List[schemas.SalesOrder])
def get_sales_orders(db: Session = Depends(get_db), skip: int = 0, limit: int = 100):
    return query(db, models.SalesOrder, offset=skip, limit=limit)

@app.get("/sales-orders/{sales_order_id}", response_model=schemas.SalesOrder)
def get_sales_order(sales_order_id: int, db: Session = Depends(get_db)):
    db_sales_order = db.query(models.SalesOrder).filter(models.SalesOrder.id == sales_order_id).first()
    if not db_sales_order:
        raise HTTPException(status_code=404, detail="Sales order not found")
    return db_sales_order

@app.put("/sales-orders/{sales_order_id}", response_model=schemas.SalesOrder)
def update_sales_order(sales_order_id: int, sales_order: schemas.SalesOrderCreate, db: Session = Depends(get_db)):
    db_sales_order = db.query(models.SalesOrder).filter(models.SalesOrder.id == sales_order_id).first()
    if not db_sales_order:
        raise HTTPException(status_code=404, detail="Sales order not found")
    for key, value in sales_order.dict().items():
        setattr(db_sales_order, key, value)
    db.commit()
    db.refresh(db_sales_order)
    return db_sales_order

@app.delete("/sales-orders/{sales_order_id}")
def delete_sales_order(sales_order_id: int, db: Session = Depends(get_db)):
    db_sales_order = db.query(models.SalesOrder).filter(models.SalesOrder.id == sales_order_id).first()
    if not db_sales_order:
        raise HTTPException(status_code=404, detail="Sales order not found")
    db.delete(db_sales_order)
    db.commit()
    return {"message": "Sales order deleted successfully"}

# --- Sale Items ---

@app.post("/sale-items/", response_model=schemas.SaleItem)
def create_sale_item(sale_item: schemas.SaleItemCreate, db: Session = Depends(get_db)):
    db_sale_item = models.SaleItem(**sale_item.dict())
    return create(db, db_sale_item)

@app.get("/sale-items/", response_model=List[schemas.SaleItem])
def get_sale_items(db: Session = Depends(get_db), skip: int = 0, limit: int = 100):
    return query(db, models.SaleItem, offset=skip, limit=limit)

@app.get("/sale-items/{sale_item_id}", response_model=schemas.SaleItem)
def get_sale_item(sale_item_id: int, db: Session = Depends(get_db)):
    db_sale_item = db.query(models.SaleItem).filter(models.SaleItem.id == sale_item_id).first()
    if not db_sale_item:
        raise HTTPException(status_code=404, detail="Sale item not found")
    return db_sale_item

@app.put("/sale-items/{sale_item_id}", response_model=schemas.SaleItem)
def update_sale_item(sale_item_id: int, sale_item: schemas.SaleItemCreate, db: Session = Depends(get_db)):
    db_sale_item = db.query(models.SaleItem).filter(models.SaleItem.id == sale_item_id).first()
    if not db_sale_item:
        raise HTTPException(status_code=404, detail="Sale item not found")
    for key, value in sale_item.dict().items():
        setattr(db_sale_item, key, value)
    db.commit()
    db.refresh(db_sale_item)
    return db_sale_item

@app.delete("/sale-items/{sale_item_id}")
def delete_sale_item(sale_item_id: int, db: Session = Depends(get_db)):
    db_sale_item = db.query(models.SaleItem).filter(models.SaleItem.id == sale_item_id).first()
    if not db_sale_item:
        raise HTTPException(status_code=404, detail="Sale item not found")
    db.delete(db_sale_item)
    db.commit()
    return {"message": "Sale item deleted successfully"}

# --- Customer Invoices ---

@app.post("/customer-invoices/", response_model=schemas.CustomerInvoice)
def create_customer_invoice(invoice: schemas.CustomerInvoiceCreate, db: Session = Depends(get_db)):
    db_invoice = models.CustomerInvoice(**invoice.dict())
    return create(db, db_invoice)

@app.get("/customer-invoices/", response_model=List[schemas.CustomerInvoice])
def get_customer_invoices(db: Session = Depends(get_db)):
    return query(db, models.CustomerInvoice)

@app.get("/customer-invoices/{invoice_id}", response_model=schemas.CustomerInvoice)
def get_customer_invoice(invoice_id: int, db: Session = Depends(get_db)):
    db_invoice = db.query(models.CustomerInvoice).filter(models.CustomerInvoice.id == invoice_id).first()
    if not db_invoice:
        raise HTTPException(status_code=404, detail="Customer invoice not found")
    return db_invoice

@app.put("/customer-invoices/{invoice_id}", response_model=schemas.CustomerInvoice)
def update_customer_invoice(invoice_id: int, invoice: schemas.CustomerInvoiceCreate, db: Session = Depends(get_db)):
    db_invoice = db.query(models.CustomerInvoice).filter(models.CustomerInvoice.id == invoice_id).first()
    if not db_invoice:
        raise HTTPException(status_code=404, detail="Customer invoice not found")
    for key, value in invoice.dict().items():
        setattr(db_invoice, key, value)
    db.commit()
    db.refresh(db_invoice)
    return db_invoice

@app.delete("/customer-invoices/{invoice_id}")
def delete_customer_invoice(invoice_id: int, db: Session = Depends(get_db)):
    db_invoice = db.query(models.CustomerInvoice).filter(models.CustomerInvoice.id == invoice_id).first()
    if not db_invoice:
        raise HTTPException(status_code=404, detail="Customer invoice not found")
    db.delete(db_invoice)
    db.commit()
    return {"message": "Customer invoice deleted successfully"}

# --- Customer Payments ---

@app.post("/customer-payments/", response_model=schemas.CustomerPayment)
def create_customer_payment(payment: schemas.CustomerPaymentCreate, db: Session = Depends(get_db)):
    db_payment = models.CustomerPayment(**payment.dict())
    return create(db, db_payment)

@app.get("/customer-payments/", response_model=List[schemas.CustomerPayment])
def get_customer_payments(db: Session = Depends(get_db)):
    return query(db, models.CustomerPayment)

@app.get("/customer-payments/{payment_id}", response_model=schemas.CustomerPayment)
def get_customer_payment(payment_id: int, db: Session = Depends(get_db)):
    db_payment = db.query(models.CustomerPayment).filter(models.CustomerPayment.id == payment_id).first()
    if not db_payment:
        raise HTTPException(status_code=404, detail="Customer payment not found")
    return db_payment

@app.put("/customer-payments/{payment_id}", response_model=schemas.CustomerPayment)
def update_customer_payment(payment_id: int, payment: schemas.CustomerPaymentCreate, db: Session = Depends(get_db)):
    db_payment = db.query(models.CustomerPayment).filter(models.CustomerPayment.id == payment_id).first()
    if not db_payment:
        raise HTTPException(status_code=404, detail="Customer payment not found")
    for key, value in payment.dict().items():
        setattr(db_payment, key, value)
    db.commit()
    db.refresh(db_payment)
    return db_payment

@app.delete("/customer-payments/{payment_id}")
def delete_customer_payment(payment_id: int, db: Session = Depends(get_db)):
    db_payment = db.query(models.CustomerPayment).filter(models.CustomerPayment.id == payment_id).first()
    if not db_payment:
        raise HTTPException(status_code=404, detail="Customer payment not found")
    db.delete(db_payment)
    db.commit()
    return {"message": "Customer payment deleted successfully"}

# --- Installment Plans ---

@app.post("/installment-plans/", response_model=schemas.InstallmentPlan)
def create_installment_plan(installment_plan: schemas.InstallmentPlanCreate, db: Session = Depends(get_db)):
    db_installment_plan = models.InstallmentPlan(**installment_plan.dict())
    return create(db, db_installment_plan)

@app.get("/installment-plans/", response_model=List[schemas.InstallmentPlan])
def get_installment_plans(db: Session = Depends(get_db)):
    return query(db, models.InstallmentPlan)

@app.get("/installment-plans/{plan_id}", response_model=schemas.InstallmentPlan)
def get_installment_plan(plan_id: int, db: Session = Depends(get_db)):
    db_installment_plan = db.query(models.InstallmentPlan).filter(models.InstallmentPlan.id == plan_id).first()
    if not db_installment_plan:
        raise HTTPException(status_code=404, detail="Installment plan not found")
    return db_installment_plan

@app.put("/installment-plans/{plan_id}", response_model=schemas.InstallmentPlan)
def update_installment_plan(plan_id: int, installment_plan: schemas.InstallmentPlanCreate, db: Session = Depends(get_db)):
    db_installment_plan = db.query(models.InstallmentPlan).filter(models.InstallmentPlan.id == plan_id).first()
    if not db_installment_plan:
        raise HTTPException(status_code=404, detail="Installment plan not found")
    for key, value in installment_plan.dict().items():
        setattr(db_installment_plan, key, value)
    db.commit()
    db.refresh(db_installment_plan)
    return db_installment_plan

@app.delete("/installment-plans/{plan_id}")
def delete_installment_plan(plan_id: int, db: Session = Depends(get_db)):
    db_installment_plan = db.query(models.InstallmentPlan).filter(models.InstallmentPlan.id == plan_id).first()
    if not db_installment_plan:
        raise HTTPException(status_code=404, detail="Installment plan not found")
    db.delete(db_installment_plan)
    db.commit()
    return {"message": "Installment plan deleted successfully"}
