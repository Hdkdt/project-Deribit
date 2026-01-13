import time
import asyncio
from celery import Celery
from db import SessionLocal
from models import Price
from deribit import get_price

celery = Celery("tasks", broker="redis://localhost:6379/0")

@celery.task
def fetch_prices():
    db = SessionLocal()
    timestamp = int(time.time())

    for ticker in ["btc_usd", "eth_usd"]:
        price = asyncio.run(get_price(ticker))
        db.add(Price(
            ticker=ticker,
            price=price,
            timestamp=timestamp
        ))

    db.commit()
    db.close()

