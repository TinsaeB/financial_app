from datetime import date
from pydantic import BaseModel, validator
from typing import List, Optional
from .models import PaymentStatusEnum

class SupplierCreate(BaseModel):
    name: str
    contact_person: str

class Supplier(SupplierCreate):
    id: int

    class Config:
        orm_mode = True

class PurchaseOrderCreate(BaseModel):
    supplier_id: int
    order_date: date

class PurchaseOrder(PurchaseOrderCreate):
    id: int

    class Config:
        orm_mode = True

class PurchaseItemCreate(BaseModel):
    purchase_order_id: int
    product: str
    quantity: int
    price: float
    delivery_status: str

class PurchaseItem(PurchaseItemCreate):
    id: int

    class Config:
        orm_mode = True

class SupplierInvoiceCreate(BaseModel):
    supplier_id: int
    invoice_number: str
    invoice_date: date
    due_date: date
    total_amount: float
    payment_status: Optional[PaymentStatusEnum] = PaymentStatusEnum.PENDING

class SupplierInvoice(SupplierInvoiceCreate):
    id: int

    class Config:
        orm_mode = True

class PaymentCreate(BaseModel):
    invoice_id: int
    payment_date: date
    amount_paid: float

class Payment(PaymentCreate):
    id: int

    class Config:
        orm_mode = True
