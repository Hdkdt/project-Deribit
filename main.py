from fastapi import FastAPI, Query
from db import SessionLocal
from models import Price

app = FastAPI()

@app.get("/prices")
def get_all(ticker: str = Query(...)):
    db = SessionLocal()
    data = db.query(Price).filter(Price.ticker == ticker).all()
    db.close()
    return data

@app.get("/prices/last")
def get_last(ticker: str = Query(...)):
    db = SessionLocal()
    data = (
        db.query(Price)
        .filter(Price.ticker == ticker)
        .order_by(Price.timestamp.desc())
        .first()
    )
    db.close()
    return data

@app.get("/prices/by-date")
def get_by_date(
    ticker: str = Query(...),
    start: int = Query(...),
    end: int = Query(...)
):
    db = SessionLocal()
    data = (
        db.query(Price)
        .filter(
            Price.ticker == ticker,
            Price.timestamp >= start,
            Price.timestamp <= end
        )
        .all()
    )
    db.close()
    return data

