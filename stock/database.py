from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import declarative_base

db = SQLAlchemy()
Base = declarative_base()

DATABASE_URI = "postgresql+psycopg2://postgres:admin123@localhost:5432/stock_management"

# Create the engine and bind it to the session
engine = create_engine(DATABASE_URI)
db_session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))

def init_db(app):
    app.teardown_appcontext(teardown_db)
    app.cli.add_command(init_database)

def teardown_db(exception=None):
    db_session.remove()

def init_database():
    from models import Consumer, Supplier, Product, Orders
    from flask import current_app
    db.drop_all(bind=engine)
    db.create_all(bind=engine)
    current_app.logger.info('Initialized the database.')

