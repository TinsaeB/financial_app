from datetime import date
from pydantic import BaseModel, validator
from typing import List, Optional
from .models import PaymentStatusEnum

class CustomerCreate(BaseModel):
    name: str
    contact_person: str

class Customer(CustomerCreate):
    id: int

    class Config:
        orm_mode = True

class SalesOrderCreate(BaseModel):
    customer_id: int
    order_date: date

class SalesOrder(SalesOrderCreate):
    id: int

    class Config:
        orm_mode = True

class SaleItemCreate(BaseModel):
    sales_order_id: int
    product: str
    quantity: int
    price: float
    delivery_status: str

class SaleItem(SaleItemCreate):
    id: int

    class Config:
        orm_mode = True

class CustomerInvoiceCreate(BaseModel):
    customer_id: int
    sales_order_id: int
    invoice_number: str
    invoice_date: date
    due_date: date
    total_amount: float
    payment_status: Optional[PaymentStatusEnum] = PaymentStatusEnum.PENDING

class CustomerInvoice(CustomerInvoiceCreate):
    id: int

    class Config:
        orm_mode = True

class CustomerPaymentCreate(BaseModel):
    invoice_id: int
    payment_date: date
    amount_paid: float

class CustomerPayment(CustomerPaymentCreate):
    id: int

    class Config:
        orm_mode = True

class InstallmentPlanCreate(BaseModel):
    invoice_id: int
    due_date: date
    amount_due: float
    status: Optional[PaymentStatusEnum] = PaymentStatusEnum.PENDING

class InstallmentPlan(InstallmentPlanCreate):
    id: int

    class Config:
        orm_mode = True
