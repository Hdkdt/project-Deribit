from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "postgresql://user:pass@localhost:5432/prices"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)
