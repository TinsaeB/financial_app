from fastapi import FastAPI, Depends, HTTPException
from . import models, schemas
from core_db.db_utils import get_db
from sqlalchemy.orm import Session

app = FastAPI()

@app.post("/suppliers/", response_model=schemas.Supplier)
def create_supplier(supplier: schemas.SupplierCreate, db: Session = Depends(get_db)):
    db_supplier = models.Supplier(**supplier.dict())
    return db.create(db_supplier)

@app.get("/suppliers/", response_model=list[schemas.Supplier])
def get_suppliers(db: Session = Depends(get_db)):
    return db.query(models.Supplier).all()

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

@app.post("/purchase-orders/", response_model=schemas.PurchaseOrder)
def create_purchase_order(purchase_order: schemas.PurchaseOrderCreate, db: Session = Depends(get_db)):
    db_purchase_order = models.PurchaseOrder(**purchase_order.dict())
    return db.create(db_purchase_order)

@app.get("/purchase-orders/", response_model=list[schemas.PurchaseOrder])
def get_purchase_orders(db: Session = Depends(get_db)):
    return db.query(models.PurchaseOrder).all()

@app.get("/purchase-orders/{purchase_order_id}", response_model=schemas.PurchaseOrder)
def get_purchase_order(purchase_order_id: int, db: Session = Depends(get_db)):
    db_purchase_order = db.query(models.PurchaseOrder).filter(models.PurchaseOrder.id == purchase_order_id).first()
    if not db_purchase_order:
        raise HTTPException(status_code=404, detail="Purchase order not found")
    return db_purchase_order

@app.post("/purchase-items/", response_model=schemas.PurchaseItem)
def create_purchase_item(purchase_item: schemas.PurchaseItemCreate, db: Session = Depends(get_db)):
    db_purchase_item = models.PurchaseItem(**purchase_item.dict())
    return db.create(db_purchase_item)

@app.get("/purchase-items/", response_model=list[schemas.PurchaseItem])
def get_purchase_items(db: Session = Depends(get_db)):
    return db.query(models.PurchaseItem).all()

@app.get("/purchase-items/{purchase_item_id}", response_model=schemas.PurchaseItem)
def get_purchase_item(purchase_item_id: int, db: Session = Depends(get_db)):
    db_purchase_item = db.query(models.PurchaseItem).filter(models.PurchaseItem.id == purchase_item_id).first()
    if not db_purchase_item:
        raise HTTPException(status_code=404, detail="Purchase item not found")
    return db_purchase_item
