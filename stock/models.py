from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Float
from sqlalchemy.orm import relationship
from sqlalchemy.orm import declarative_base
from database import Base

Base = declarative_base()
engine = create_engine("postgresql+psycopg2://postgres:admin123@localhost:5432/stock_management")
Base.metadata.bind = engine

class Consumer(Base):
    __tablename__ = 'consumer'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)
    orders = relationship('Orders', back_populates='consumer', cascade='all, delete')


class Supplier(Base):
    __tablename__ = 'supplier'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)
    products = relationship('Product', back_populates='supplier', cascade='all, delete')


class Product(Base):
    __tablename__ = 'product'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    price = Column(Float)
    supplier_id = Column(Integer, ForeignKey('supplier.id', ondelete='CASCADE', onupdate='CASCADE'))
    supplier = relationship('Supplier', back_populates='products')


class Orders(Base):
    __tablename__ = 'orders'
    id = Column(Integer, primary_key=True)
    quantity = Column(Integer)
    consumer_id = Column(Integer, ForeignKey('consumer.id', ondelete='CASCADE', onupdate='CASCADE'))
    consumer = relationship('Consumer', back_populates='orders')
    supplier_id = Column(Integer, ForeignKey('supplier.id', ondelete='CASCADE', onupdate='CASCADE'))
    supplier = relationship('Supplier')
    product_id = Column(Integer, ForeignKey('product.id', ondelete='CASCADE', onupdate='CASCADE'))
    product = relationship('Product')

if __name__ == '__main__':
    Base.metadata.create_all(engine)
