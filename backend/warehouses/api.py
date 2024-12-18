from fastapi import FastAPI, Depends, HTTPException
from . import models, schemas
from core_db.db_utils import get_db
from sqlalchemy.orm import Session

app = FastAPI()

@app.post("/warehouses/", response_model=schemas.Warehouse)
def create_warehouse(warehouse: schemas.WarehouseCreate, db: Session = Depends(get_db)):
    db_warehouse = models.Warehouse(**warehouse.dict())
    return db.create(db_warehouse)

@app.get("/warehouses/", response_model=list[schemas.Warehouse])
def get_warehouses(db: Session = Depends(get_db)):
    return db.query(models.Warehouse).all()

@app.get("/warehouses/{warehouse_id}", response_model=schemas.Warehouse)
def get_warehouse(warehouse_id: int, db: Session = Depends(get_db)):
    db_warehouse = db.query(models.Warehouse).filter(models.Warehouse.id == warehouse_id).first()
    if not db_warehouse:
        raise HTTPException(status_code=404, detail="Warehouse not found")
    return db_warehouse

@app.put("/warehouses/{warehouse_id}", response_model=schemas.Warehouse)
def update_warehouse(warehouse_id: int, warehouse: schemas.WarehouseCreate, db: Session = Depends(get_db)):
    db_warehouse = db.query(models.Warehouse).filter(models.Warehouse.id == warehouse_id).first()
    if not db_warehouse:
        raise HTTPException(status_code=404, detail="Warehouse not found")
    for key, value in warehouse.dict().items():
        setattr(db_warehouse, key, value)
    db.commit()
    db.refresh(db_warehouse)
    return db_warehouse

@app.delete("/warehouses/{warehouse_id}")
def delete_warehouse(warehouse_id: int, db: Session = Depends(get_db)):
    db_warehouse = db.query(models.Warehouse).filter(models.Warehouse.id == warehouse_id).first()
    if not db_warehouse:
        raise HTTPException(status_code=404, detail="Warehouse not found")
    db.delete(db_warehouse)
    db.commit()
    return {"message": "Warehouse deleted successfully"}

@app.post("/inventory-items/", response_model=schemas.InventoryItem)
def create_inventory_item(inventory_item: schemas.InventoryItemCreate, db: Session = Depends(get_db)):
    db_inventory_item = models.InventoryItem(**inventory_item.dict())
    return db.create(db_inventory_item)

@app.get("/inventory-items/", response_model=list[schemas.InventoryItem])
def get_inventory_items(db: Session = Depends(get_db)):
    return db.query(models.InventoryItem).all()

@app.get("/inventory-items/{inventory_item_id}", response_model=schemas.InventoryItem)
def get_inventory_item(inventory_item_id: int, db: Session = Depends(get_db)):
    db_inventory_item = db.query(models.InventoryItem).filter(models.InventoryItem.id == inventory_item_id).first()
    if not db_inventory_item:
        raise HTTPException(status_code=404, detail="Inventory item not found")
    return db_inventory_item

@app.get("/warehouses/{warehouse_id}/inventory", response_model=list[schemas.InventoryItem])
def get_warehouse_inventory(warehouse_id: int, db: Session = Depends(get_db)):
    return db.query(models.InventoryItem).filter(models.InventoryItem.warehouse_id == warehouse_id).all()

@app.post("/stock-movements/", response_model=schemas.StockMovement)
def create_stock_movement(stock_movement: schemas.StockMovementCreate, db: Session = Depends(get_db)):
    db_stock_movement = models.StockMovement(**stock_movement.dict())
    return db.create(db_stock_movement)

@app.get("/stock-movements/", response_model=list[schemas.StockMovement])
def get_stock_movements(db: Session = Depends(get_db)):
    return db.query(models.StockMovement).all()

@app.get("/stock-movements/{stock_movement_id}", response_model=schemas.StockMovement)
def get_stock_movement(stock_movement_id: int, db: Session = Depends(get_db)):
    db_stock_movement = db.query(models.StockMovement).filter(models.StockMovement.id == stock_movement_id).first()
    if not db_stock_movement:
        raise HTTPException(status_code=404, detail="Stock movement not found")
    return db_stock_movement
