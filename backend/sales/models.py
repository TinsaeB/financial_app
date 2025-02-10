from sqlalchemy import Column, Integer, String, Date, ForeignKey, Float, Enum
from sqlalchemy.orm import relationship
from core_db.db_utils import Base
import enum

class Customer(Base):
    __tablename__ = "customers"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    contact_person = Column(String)

    sales_orders = relationship("SalesOrder", back_populates="customer")
    invoices = relationship("CustomerInvoice", back_populates="customer")

class SalesOrder(Base):
    __tablename__ = "sales_orders"

    id = Column(Integer, primary_key=True, index=True)
    customer_id = Column(Integer, ForeignKey("customers.id"))
    order_date = Column(Date)

    customer = relationship("Customer", back_populates="sales_orders")
    items = relationship("SaleItem", back_populates="sales_order")

class SaleItem(Base):
    __tablename__ = "sale_items"

    id = Column(Integer, primary_key=True, index=True)
    sales_order_id = Column(Integer, ForeignKey("sales_orders.id"))
    product = Column(String)
    quantity = Column(Integer)
    price = Column(Float)
    delivery_status = Column(String)

    sales_order = relationship("SalesOrder", back_populates="items")

class PaymentStatusEnum(enum.Enum):
    PENDING = "PENDING"
    PAID = "PAID"
    PARTIALLY_PAID = "PARTIALLY_PAID"

class CustomerInvoice(Base):
    __tablename__ = "customer_invoices"

    id = Column(Integer, primary_key=True, index=True)
    customer_id = Column(Integer, ForeignKey("customers.id"))
    sales_order_id = Column(Integer, ForeignKey("sales_orders.id"))
    invoice_number = Column(String)
    invoice_date = Column(Date)
    due_date = Column(Date)
    total_amount = Column(Float)
    payment_status = Column(Enum(PaymentStatusEnum), default=PaymentStatusEnum.PENDING)

    customer = relationship("Customer", back_populates="invoices")
    sales_order = relationship("SalesOrder")
    payments = relationship("CustomerPayment", back_populates="invoice")

class CustomerPayment(Base):
    __tablename__ = "customer_payments"

    id = Column(Integer, primary_key=True, index=True)
    invoice_id = Column(Integer, ForeignKey("customer_invoices.id"))
    payment_date = Column(Date)
    amount_paid = Column(Float)

    invoice = relationship("CustomerInvoice", back_populates="payments")

class InstallmentPlan(Base):
    __tablename__ = "installment_plans"

    id = Column(Integer, primary_key=True, index=True)
    invoice_id = Column(Integer, ForeignKey("customer_invoices.id"))
    due_date = Column(Date)
    amount_due = Column(Float)
    status = Column(Enum(PaymentStatusEnum), default=PaymentStatusEnum.PENDING)

    invoice = relationship("CustomerInvoice")
