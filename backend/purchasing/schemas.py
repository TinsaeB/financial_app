from pydantic import BaseModel
from typing import List

class SupplierCreate(BaseModel):
    name: str
    contact_person: str

class Supplier(SupplierCreate):
    id: int

class PurchaseOrderCreate(BaseModel):
    supplier_id: int
    order_date: str

class PurchaseOrder(PurchaseOrderCreate):
    id: int

class PurchaseItemCreate(BaseModel):
    purchase_order_id: int
    product: str
    quantity: int
    price: float
    delivery_status: str

class PurchaseItem(PurchaseItemCreate):
    id: int
