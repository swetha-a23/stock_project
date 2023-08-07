from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Create the engine
engine = create_engine("postgresql://postgres:admin123@localhost:5432/Stock_management")

# Create a session factory
Session = sessionmaker(bind=engine)

# Export the engine and session factory for easy access
__all__ = ['engine', 'Session']

