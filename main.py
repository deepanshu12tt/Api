from typing import List
from fetch import Trade
import uvicorn
from fastapi import FastAPI

api=FastAPI()
db:List[Trade]= [
    Trade(
        asset_class="Bond",
        counterparty="available",
        instrument_id="AAPL",
        instrument_name="stocks",
        trade_date_time= 3-12-2020,
        trade_id=12345,
        trader="Deepanshu Verma",
        buysell="buy",
        price=30000,
        quantity=100
    ),
Trade(
        asset_class="Bond",
        counterparty=" not available",
        instrument_id="AAPL",
        instrument_name="stocks",
        trade_date_time= 30-2-2019,
        trade_id=32873,
        trader="Raj Verma",
        buysell="buy",
        price=3000,
        quantity=10
    ),
Trade(
        asset_class="equity",
        counterparty="available",
        instrument_id="AAPL",
        instrument_name="stocks",
        trade_date_time= 24-9-2020,
        trade_id=15897,
        trader="Alex hales",
        buysell="sell",
        price=10000,
        quantity=100
    ),
Trade(
        asset_class="Bond",
        counterparty=" not available",
        instrument_id="AAPL",
        instrument_name="stocks",
        trade_date_time= 12-12-2020,
        trade_id=45276,
        trader="marnus labuschane",
        buysell="sell",
        price=90865,
        quantity=289
    ),
Trade(
        asset_class="equity",
        counterparty="not available",
        instrument_id="AMZN",
        instrument_name="stocks",
        trade_date_time= 9-9-2022,
        trade_id=28783,
        trader="Roman Reigns",
        buysell="buy",
        price=300,
        quantity=10
    ),
Trade(
        asset_class="Mutual fund",
        counterparty="available",
        instrument_id="AAPL",
        instrument_name="stocks",
        trade_date_time= 30-12-2021,
        trade_id=34598,
        trader="Akshit Rawat",
        buysell="Buy",
        price=300000,
        quantity=900
    ),
Trade(
        asset_class="Stocks",
        counterparty="not available",
        instrument_id="AAPL",
        instrument_name="stocks",
        trade_date_time= 15-1-2021,
        trade_id=12565,
        trader="Jaspreet Singh",
        buysell="sell",
        price=90000,
        quantity=1000
    ),
Trade(
        asset_class="equity",
        counterparty="not available",
        instrument_id="AMZN",
        instrument_name="stocks",
        trade_date_time= 19-12-2018,
        trade_id=58754,
        trader="Shivankit Raghav",
        buysell="sell",
        price=8754,
        quantity=65
    ),
Trade(
        asset_class="stocks",
        counterparty="available",
        instrument_id="TSLA",
        instrument_name="stocks",
        trade_date_time= 5-6-2013,
        trade_id=98745,
        trader="Deepanshu Verma",
        buysell="buy",
        price=5567,
        quantity=78
    ),
Trade(
        asset_class="Bond",
        counterparty="available",
        instrument_id="TSLA",
        instrument_name="stocks",
        trade_date_time= 28-6-2000,
        trade_id=98643,
        trader="Ankit Pandey",
        buysell="sell",
        price=3000000,
        quantity=308
    ),
]
@api.get("/")
async def fetch_trade():
    return db;
@api.get("/items/{trade_id}")
async def single_fetch(trade_id:int):
    return {"trade_id":trade_id}
@api.get("/")
async def get_asset(asset_class:str):
    return db[asset_class]
@api.get("/")
async def get_time(trade_date_time:int):
    a=max(trade_date_time)
    return db[a]
@api.get("/")
async def get_price_min(price:int):
    return db[min(price)]
@api.get("/")
async def get_start(trade_date_time:int):
    return db[min(trade_date_time)]
@api.get("/")
async def get_type(buysell:str):
    return db[buysell]
@api.get("/")
async def get_sort(Trade:Trade):
    a=sorted(Trade)
    return db[a]
@api.get("/")
def read_posts(page_num:int=1,page_size:int=2):
    start=(page_num-1)*page_size
    end=start+page_size
    return db[start:end]
uvicorn.run(api)