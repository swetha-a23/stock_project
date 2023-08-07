from models import Consumer, Supplier, Product, Orders
from database import db_session

# DAO functions for Consumer
def get_consumer_by_id(consumer_id):
    return db_session.query(Consumer).filter(Consumer.id == consumer_id).first()

def get_all_consumers():
    return db_session.query(Consumer).all()

def create_consumer(name, email):
    consumer = Consumer(name=name, email=email)
    db_session.add(consumer)
    db_session.commit()
    return consumer

def update_consumer(consumer_id, name, email):
    consumer = get_consumer_by_id(consumer_id)
    if consumer:
        consumer.name = name
        consumer.email = email
        db_session.commit()
    return consumer

def delete_consumer(consumer_id):
    consumer = get_consumer_by_id(consumer_id)
    if consumer:
        db_session.delete(consumer)
        db_session.commit()
    return consumer

# DAO functions for Supplier
def get_supplier_by_id(supplier_id):
    return db_session.query(Supplier).filter(Supplier.id == supplier_id).first()

def get_all_suppliers():
    return db_session.query(Supplier).all()

def create_supplier(name, email):
    supplier = Supplier(name=name, email=email)
    db_session.add(supplier)
    db_session.commit()
    return supplier

def update_supplier(supplier_id, name, email):
    supplier = get_supplier_by_id(supplier_id)
    if supplier:
        supplier.name = name
        supplier.email = email
        db_session.commit()
    return supplier

def delete_supplier(supplier_id):
    supplier = get_supplier_by_id(supplier_id)
    if supplier:
        db_session.delete(supplier)
        db_session.commit()
    return supplier


# DAO functions for Product

def get_product_by_id(product_id):
    return db_session.query(Product).filter(Product.id == product_id).first()

def get_all_products():
    return db_session.query(Product).all()

def create_product(name, price, supplier_id):
    product = Product(name=name, price=price, supplier_id=supplier_id)
    db_session.add(product)
    db_session.commit()
    return product

def update_product(product_id, name, price, supplier_id):
    product = get_product_by_id(product_id)
    if product:
        product.name = name
        product.price = price
        product.supplier_id = supplier_id
        db_session.commit()
    return product

def delete_product(product_id):
    product = get_product_by_id(product_id)
    if product:
        db_session.delete(product)
        db_session.commit()
    return product

# DAO functions for Order
def get_order_by_id(order_id):
    return db_session.query(Orders).filter(Orders.id == order_id).first()

def get_all_orders():
    return db_session.query(Orders).all()

def create_order(quantity, consumer_id, supplier_id,product_id):
    order = Orders(quantity=quantity, consumer_id=consumer_id,supplier_id=supplier_id, product_id=product_id)
    db_session.add(order)
    db_session.commit()
    return order

def update_order(order_id,quantity, consumer_id, supplier_id,product_id):
    order = get_order_by_id(order_id)
    if order:
        order.quantity=quantity
        order.consumer_id = consumer_id
        order.supplier_id=supplier_id
        order.product_id = product_id
        db_session.commit()
    return order

def delete_order(order_id):
    order = get_order_by_id(order_id)
    if order:
        db_session.delete(order)
        db_session.commit()
    return order
