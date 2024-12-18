from fastapi import FastAPI, Depends, HTTPException
from . import models, schemas
from core_db.db_utils import get_db
from sqlalchemy.orm import Session

app = FastAPI()

@app.post("/customers/", response_model=schemas.Customer)
def create_customer(customer: schemas.CustomerCreate, db: Session = Depends(get_db)):
    db_customer = models.Customer(**customer.dict())
    return db.create(db_customer)

@app.get("/customers/", response_model=list[schemas.Customer])
def get_customers(db: Session = Depends(get_db)):
    return db.query(models.Customer).all()

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

@app.post("/sales-orders/", response_model=schemas.SalesOrder)
def create_sales_order(sales_order: schemas.SalesOrderCreate, db: Session = Depends(get_db)):
    db_sales_order = models.SalesOrder(**sales_order.dict())
    return db.create(db_sales_order)

@app.get("/sales-orders/", response_model=list[schemas.SalesOrder])
def get_sales_orders(db: Session = Depends(get_db)):
    return db.query(models.SalesOrder).all()

@app.get("/sales-orders/{sales_order_id}", response_model=schemas.SalesOrder)
def get_sales_order(sales_order_id: int, db: Session = Depends(get_db)):
    db_sales_order = db.query(models.SalesOrder).filter(models.SalesOrder.id == sales_order_id).first()
    if not db_sales_order:
        raise HTTPException(status_code=404, detail="Sales order not found")
    return db_sales_order

@app.post("/sale-items/", response_model=schemas.SaleItem)
def create_sale_item(sale_item: schemas.SaleItemCreate, db: Session = Depends(get_db)):
    db_sale_item = models.SaleItem(**sale_item.dict())
    return db.create(db_sale_item)

@app.get("/sale-items/", response_model=list[schemas.SaleItem])
def get_sale_items(db: Session = Depends(get_db)):
    return db.query(models.SaleItem).all()

@app.get("/sale-items/{sale_item_id}", response_model=schemas.SaleItem)
def get_sale_item(sale_item_id: int, db: Session = Depends(get_db)):
    db_sale_item = db.query(models.SaleItem).filter(models.SaleItem.id == sale_item_id).first()
    if not db_sale_item:
        raise HTTPException(status_code=404, detail="Sale item not found")
    return db_sale_item
