from sqlalchemy import Column, Integer, String, Date, ForeignKey, Float, Enum
from sqlalchemy.orm import relationship
from core_db.db_utils import Base
import enum

class Supplier(Base):
    __tablename__ = "suppliers"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    contact_person = Column(String)

    purchase_orders = relationship("PurchaseOrder", back_populates="supplier")
    invoices = relationship("SupplierInvoice", back_populates="supplier")

class PurchaseOrder(Base):
    __tablename__ = "purchase_orders"

    id = Column(Integer, primary_key=True, index=True)
    supplier_id = Column(Integer, ForeignKey("suppliers.id"))
    order_date = Column(Date)

    supplier = relationship("Supplier", back_populates="purchase_orders")
    items = relationship("PurchaseItem", back_populates="purchase_order")

class PurchaseItem(Base):
    __tablename__ = "purchase_items"

    id = Column(Integer, primary_key=True, index=True)
    purchase_order_id = Column(Integer, ForeignKey("purchase_orders.id"))
    product = Column(String)
    quantity = Column(Integer)
    price = Column(Float)
    delivery_status = Column(String)

    purchase_order = relationship("PurchaseOrder", back_populates="items")

class PaymentStatusEnum(enum.Enum):
    PENDING = "PENDING"
    PAID = "PAID"
    OVERDUE = "OVERDUE"

class SupplierInvoice(Base):
    __tablename__ = "supplier_invoices"

    id = Column(Integer, primary_key=True, index=True)
    supplier_id = Column(Integer, ForeignKey("suppliers.id"))
    invoice_number = Column(String)
    invoice_date = Column(Date)
    due_date = Column(Date)
    total_amount = Column(Float)
    payment_status = Column(Enum(PaymentStatusEnum), default=PaymentStatusEnum.PENDING)

    supplier = relationship("Supplier", back_populates="invoices")
    payments = relationship("Payment", back_populates="invoice")

class Payment(Base):
    __tablename__ = "payments"

    id = Column(Integer, primary_key=True, index=True)
    invoice_id = Column(Integer, ForeignKey("supplier_invoices.id"))
    payment_date = Column(Date)
    amount_paid = Column(Float)

    invoice = relationship("SupplierInvoice", back_populates="payments")
