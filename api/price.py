import time
from typing import Dict, Any

import requests
from fastapi import APIRouter
from starlette.responses import JSONResponse

router = APIRouter(tags=["Price"], prefix="/price")


@router.get("/{symbol}", response_model=Dict[Any, Any])
def get_historical_price(
        symbol: str
):
    current_timestamp = int(time.time() * 1000)
    url = "https://api.redstone.finance/prices"
    params = {
        "symbol": symbol,
        "provider": "redstone",
        "toTimestamp": current_timestamp,
        "limit": 10
    }

    # Send the GET request
    response = requests.get(url, params=params)

    if response.status_code == 200:
        data = response.json()  # Parse the response as JSON
        res = [{"symbol": index["symbol"], "value": index["value"], "timestamp": index["timestamp"]} for index in data]
        print(res)
        return JSONResponse(content={"Res": res})
    else:
        print(f"Request failed with status code {response.status_code}")
        return JSONResponse(content={"Res": "Error"})
