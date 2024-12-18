from pydantic import BaseModel
from typing import List

class CustomerCreate(BaseModel):
    name: str
    contact_person: str

class Customer(CustomerCreate):
    id: int

class SalesOrderCreate(BaseModel):
    customer_id: int
    order_date: str

class SalesOrder(SalesOrderCreate):
    id: int

class SaleItemCreate(BaseModel):
    sales_order_id: int
    product: str
    quantity: int
    price: float
    delivery_status: str

class SaleItem(SaleItemCreate):
    id: int
