from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from core_db.db_utils import get_db, create, query
from . import models, schemas

app = APIRouter()

# --- Suppliers ---

@app.post("/suppliers/", response_model=schemas.Supplier)
def create_supplier(supplier: schemas.SupplierCreate, db: Session = Depends(get_db)):
    db_supplier = models.Supplier(**supplier.dict())
    return create(db, db_supplier)

@app.get("/suppliers/", response_model=List[schemas.Supplier])
def get_suppliers(db: Session = Depends(get_db), skip: int = 0, limit: int = 100):
    return query(db, models.Supplier, offset=skip, limit=limit)

@app.get("/suppliers/{supplier_id}", response_model=schemas.Supplier)
def get_supplier(supplier_id: int, db: Session = Depends(get_db)):
    db_supplier = db.query(models.Supplier).filter(models.Supplier.id == supplier_id).first()
    if not db_supplier:
        raise HTTPException(status_code=404, detail="Supplier not found")
    return db_supplier

@app.put("/suppliers/{supplier_id}", response_model=schemas.Supplier)
def update_supplier(supplier_id: int, supplier: schemas.SupplierCreate, db: Session = Depends(get_db)):
    db_supplier = db.query(models.Supplier).filter(models.Supplier.id == supplier_id).first()
    if not db_supplier:
        raise HTTPException(status_code=404, detail="Supplier not found")
    for key, value in supplier.dict().items():
        setattr(db_supplier, key, value)
    db.commit()
    db.refresh(db_supplier)
    return db_supplier

@app.delete("/suppliers/{supplier_id}")
def delete_supplier(supplier_id: int, db: Session = Depends(get_db)):
    db_supplier = db.query(models.Supplier).filter(models.Supplier.id == supplier_id).first()
    if not db_supplier:
        raise HTTPException(status_code=404, detail="Supplier not found")
    db.delete(db_supplier)
    db.commit()
    return {"message": "Supplier deleted successfully"}

# --- Purchase Orders ---

@app.post("/purchase-orders/", response_model=schemas.PurchaseOrder)
def create_purchase_order(purchase_order: schemas.PurchaseOrderCreate, db: Session = Depends(get_db)):
    db_purchase_order = models.PurchaseOrder(**purchase_order.dict())
    return create(db, db_purchase_order)

@app.get("/purchase-orders/", response_model=List[schemas.PurchaseOrder])
def get_purchase_orders(db: Session = Depends(get_db), skip: int = 0, limit: int = 100):
    return query(db, models.PurchaseOrder, offset=skip, limit=limit)

@app.get("/purchase-orders/{purchase_order_id}", response_model=schemas.PurchaseOrder)
def get_purchase_order(purchase_order_id: int, db: Session = Depends(get_db)):
    db_purchase_order = db.query(models.PurchaseOrder).filter(models.PurchaseOrder.id == purchase_order_id).first()
    if not db_purchase_order:
        raise HTTPException(status_code=404, detail="Purchase order not found")
    return db_purchase_order

@app.put("/purchase-orders/{purchase_order_id}", response_model=schemas.PurchaseOrder)
def update_purchase_order(purchase_order_id: int, purchase_order: schemas.PurchaseOrderCreate, db: Session = Depends(get_db)):
    db_purchase_order = db.query(models.PurchaseOrder).filter(models.PurchaseOrder.id == purchase_order_id).first()
    if not db_purchase_order:
        raise HTTPException(status_code=404, detail="Purchase order not found")
    for key, value in purchase_order.dict().items():
        setattr(db_purchase_order, key, value)
    db.commit()
    db.refresh(db_purchase_order)
    return db_purchase_order

@app.delete("/purchase-orders/{purchase_order_id}")
def delete_purchase_order(purchase_order_id: int, db: Session = Depends(get_db)):
    db_purchase_order = db.query(models.PurchaseOrder).filter(models.PurchaseOrder.id == purchase_order_id).first()
    if not db_purchase_order:
        raise HTTPException(status_code=404, detail="Purchase order not found")
    db.delete(db_purchase_order)
    db.commit()
    return {"message": "Purchase order deleted successfully"}

# --- Purchase Items ---

@app.post("/purchase-items/", response_model=schemas.PurchaseItem)
def create_purchase_item(purchase_item: schemas.PurchaseItemCreate, db: Session = Depends(get_db)):
    db_purchase_item = models.PurchaseItem(**purchase_item.dict())
    return create(db, db_purchase_item)

@app.get("/purchase-items/", response_model=List[schemas.PurchaseItem])
def get_purchase_items(db: Session = Depends(get_db), skip: int = 0, limit: int = 100):
    return query(db, models.PurchaseItem, offset=skip, limit=limit)

@app.get("/purchase-items/{purchase_item_id}", response_model=schemas.PurchaseItem)
def get_purchase_item(purchase_item_id: int, db: Session = Depends(get_db)):
    db_purchase_item = db.query(models.PurchaseItem).filter(models.PurchaseItem.id == purchase_item_id).first()
    if not db_purchase_item:
        raise HTTPException(status_code=404, detail="Purchase item not found")
    return db_purchase_item

@app.put("/purchase-items/{purchase_item_id}", response_model=schemas.PurchaseItem)
def update_purchase_item(purchase_item_id: int, purchase_item: schemas.PurchaseItemCreate, db: Session = Depends(get_db)):
    db_purchase_item = db.query(models.PurchaseItem).filter(models.PurchaseItem.id == purchase_item_id).first()
    if not db_purchase_item:
        raise HTTPException(status_code=404, detail="Purchase item not found")
    for key, value in purchase_item.dict().items():
        setattr(db_purchase_item, key, value)
    db.commit()
    db.refresh(db_purchase_item)
    return db_purchase_item

@app.delete("/purchase-items/{purchase_item_id}")
def delete_purchase_item(purchase_item_id: int, db: Session = Depends(get_db)):
    db_purchase_item = db.query(models.PurchaseItem).filter(models.PurchaseItem.id == purchase_item_id).first()
    if not db_purchase_item:
        raise HTTPException(status_code=404, detail="Purchase item not found")
    db.delete(db_purchase_item)
    db.commit()
    return {"message": "Purchase item deleted successfully"}

# --- Supplier Invoices ---

@app.post("/supplier-invoices/", response_model=schemas.SupplierInvoice)
def create_supplier_invoice(invoice: schemas.SupplierInvoiceCreate, db: Session = Depends(get_db)):
    db_invoice = models.SupplierInvoice(**invoice.dict())
    return create(db, db_invoice)

@app.get("/supplier-invoices/", response_model=List[schemas.SupplierInvoice])
def get_supplier_invoices(db: Session = Depends(get_db), skip: int = 0, limit: int = 100):
    return query(db, models.SupplierInvoice, offset=skip, limit=limit)

@app.get("/supplier-invoices/{invoice_id}", response_model=schemas.SupplierInvoice)
def get_supplier_invoice(invoice_id: int, db: Session = Depends(get_db)):
    db_invoice = db.query(models.SupplierInvoice).filter(models.SupplierInvoice.id == invoice_id).first()
    if not db_invoice:
        raise HTTPException(status_code=404, detail="Supplier invoice not found")
    return db_invoice

@app.put("/supplier-invoices/{invoice_id}", response_model=schemas.SupplierInvoice)
def update_supplier_invoice(invoice_id: int, invoice: schemas.SupplierInvoiceCreate, db: Session = Depends(get_db)):
    db_invoice = db.query(models.SupplierInvoice).filter(models.SupplierInvoice.id == invoice_id).first()
    if not db_invoice:
        raise HTTPException(status_code=404, detail="Supplier invoice not found")
    for key, value in invoice.dict().items():
        setattr(db_invoice, key, value)
    db.commit()
    db.refresh(db_invoice)
    return db_invoice

@app.delete("/supplier-invoices/{invoice_id}")
def delete_supplier_invoice(invoice_id: int, db: Session = Depends(get_db)):
    db_invoice = db.query(models.SupplierInvoice).filter(models.SupplierInvoice.id == invoice_id).first()
    if not db_invoice:
        raise HTTPException(status_code=404, detail="Supplier invoice not found")
    db.delete(db_invoice)
    db.commit()
    return {"message": "Supplier invoice deleted successfully"}

# --- Payments ---

@app.post("/payments/", response_model=schemas.Payment)
def create_payment(payment: schemas.PaymentCreate, db: Session = Depends(get_db)):
    db_payment = models.Payment(**payment.dict())
    return create(db, db_payment)

@app.get("/payments/", response_model=List[schemas.Payment])
def get_payments(db: Session = Depends(get_db), skip: int = 0, limit: int = 100):
    return query(db, models.Payment, offset=skip, limit=limit)

@app.get("/payments/{payment_id}", response_model=schemas.Payment)
def get_payment(payment_id: int, db: Session = Depends(get_db)):
    db_payment = db.query(models.Payment).filter(models.Payment.id == payment_id).first()
    if not db_payment:
        raise HTTPException(status_code=404, detail="Payment not found")
    return db_payment

@app.put("/payments/{payment_id}", response_model=schemas.Payment)
def update_payment(payment_id: int, payment: schemas.PaymentCreate, db: Session = Depends(get_db)):
    db_payment = db.query(models.Payment).filter(models.Payment.id == payment_id).first()
    if not db_payment:
        raise HTTPException(status_code=404, detail="Payment not found")
    for key, value in payment.dict().items():
        setattr(db_payment, key, value)
    db.commit()
    db.refresh(db_payment)
    return db_payment

@app.delete("/payments/{payment_id}")
def delete_payment(payment_id: int, db: Session = Depends(get_db)):
    db_payment = db.query(models.Payment).filter(models.Payment.id == payment_id).first()
    if not db_payment:
        raise HTTPException(status_code=404, detail="Payment not found")
    db.delete(db_payment)
    db.commit()
    return {"message": "Payment deleted successfully"}
