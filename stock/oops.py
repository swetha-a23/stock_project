from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:admin123@localhost/Stock_management?port=5432"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

class Consumer(db.Model):
    __tablename__ = "consumer"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    email = db.Column(db.String(255))

    def __init__(self, name, email):
        self.name = name
        self.email = email

    def __str__(self):
        return f"Consumer(id={self.id}, name={self.name}, email={self.email})"

class Supplier(db.Model):
    __tablename__ = "supplier"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    email = db.Column(db.String(255))

    def __init__(self, name, email):
        self.name = name
        self.email = email

    def __str__(self):
        return f"Supplier(id={self.id}, name={self.name}, email={self.email})"

class Product(db.Model):
    __tablename__ = "product"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    price = db.Column(db.Float) 
    supplier_id = db.Column(db.Integer, db.ForeignKey('supplier.id'))
    supplier = db.relationship('Supplier', backref=db.backref('products', lazy=True))

    def __init__(self, name, price, supplier):  
        self.name = name
        self.price = price
        self.supplier = supplier

    def __str__(self):
        return f"Product(id={self.id}, name={self.name}, price={self.price}, supplier={self.supplier})"


class Orders(db.Model):
    __tablename__ = "orders"

    id = db.Column(db.Integer, primary_key=True)
    consumer_id = db.Column(db.Integer, db.ForeignKey('consumer.id'))
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'))
    consumer = db.relationship('Consumer', backref=db.backref('orders', lazy=True))
    product = db.relationship('Product', backref=db.backref('orders', lazy=True))

    def __init__(self, consumer, product):
        self.consumer = consumer
        self.product = product

    def __str__(self):
        return f"Orders(id={self.id}, consumer={self.consumer}, product={self.product})"

if __name__ == "__main__":
    app.run()
