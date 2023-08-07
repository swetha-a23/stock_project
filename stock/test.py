import unittest
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from graphene.test import Client
from main import app
from schemas import schema
from models import Consumer, Supplier, Product, Order

class AppTestCase(unittest.TestCase):
    def setUp(self):
        # Set up Flask app and database
        self.app = app.test_client()
        self.db = SQLAlchemy(app)

        # Create the test database tables
        with app.app_context():
            self.db.create_all()

    def tearDown(self):
        # Clean up the test database tables
        with app.app_context():
            self.db.session.remove()
            self.db.drop_all()

    def test_get_all_consumers(self):
        # Create some test consumers
        consumer1 = Consumer(name="Anna")
        consumer2 = Consumer(name="Tiana")
        self.db.session.add_all([consumer1, consumer2])
        self.db.session.commit()

        # Perform the GraphQL query
        client = Client(schema)
        result = client.execute('{ getAllConsumers { id, name } }')

        # Check the query result
        self.assertEqual(result['data']['getAllConsumers'], [
            {'id': str(consumer1.id), 'name': consumer1.name},
            {'id': str(consumer2.id), 'name': consumer2.name}
        ])

    # Add more test cases for other resolvers and mutations...

if __name__ == '__main__':
    unittest.main()

