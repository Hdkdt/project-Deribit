import aiohttp

async def get_price(ticker: str) -> float:
    url = "https://www.deribit.com/api/v2/public/get_index_price"
    params = {"index_name": ticker}

    async with aiohttp.ClientSession() as session:
        async with session.get(url, params=params) as resp:
            data = await resp.json()
            return data["result"]["index_price"]

