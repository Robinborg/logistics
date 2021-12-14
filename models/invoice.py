from sqlalchemy import Table, Column, Integer, ForeignKey, String, create_engine
from sqlalchemy.orm import relationship, declarative_base
from models import Base


class Invoice(Base):
    __tablename__ = 'invoice_table'

    id = Column(Integer, primary_key = True)
    customer_id = Column(ForeignKey("customer_table.id"))
    products_invoice_relationship = relationship("ProductsInvoice",
                                                  back_populates = "invoice_relationship")
    customer_relationship = relationship("Customer",
                                         back_populates="invoice_relationship")


