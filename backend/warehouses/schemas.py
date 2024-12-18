from pydantic import BaseModel
from typing import List

class WarehouseCreate(BaseModel):
    name: str
    location: str
    capacity: int

class Warehouse(WarehouseCreate):
    id: int

class InventoryItemCreate(BaseModel):
    warehouse_id: int
    product: str
    quantity: int
    minimum_stock_level: int

class InventoryItem(InventoryItemCreate):
    id: int

class StockMovementCreate(BaseModel):
    item_id: int
    from_warehouse_id: int
    to_warehouse_id: int
    quantity: int
    movement_date: str

class StockMovement(StockMovementCreate):
    id: int
