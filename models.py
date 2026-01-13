from sqlalchemy import Column, Integer, String, Numeric, BigInteger
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Price(Base):
    __tablename__ = "prices"

    id = Column(Integer, primary_key=True)
    ticker = Column(String)
    price = Column(Numeric)
    timestamp = Column(BigInteger)

