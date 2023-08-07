from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from strawberry.flask.views import GraphQLView
from schemas import schema
from database import init_db

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql+psycopg2://postgres:admin123@localhost:5432/stock_management"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

class StockManagementApp:
    def __init__(self, database_uri):
        self.app = Flask(__name__)
        self.app.config["SQLALCHEMY_DATABASE_URI"] = database_uri
        self.app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

        try:
            init_db(self.app)
        except Exception as e:
            print(f"An error occurred while initializing the database: {str(e)}")

        self.setup_routes()

    def setup_routes(self):
        self.app.add_url_rule(
            "/graphql",
            view_func=GraphQLView.as_view("graphql", schema=schema),
        )

    def run(self):
        try:
            self.app.run()
        except Exception as e:
            print(f"An error occurred while running the application: {str(e)}")


if __name__ == "__main__":
    stock_management_app = StockManagementApp(app.config["SQLALCHEMY_DATABASE_URI"])
    stock_management_app.run()
