from typing import Dict, List

from starlette.responses import JSONResponse
from web3 import Web3

from chainlink.abi import AggregatorV3Interface


def get_price(rpc: str, addresses: Dict[str, str]) -> JSONResponse:
    # Change this to use your own RPC URL
    web3 = Web3(Web3.HTTPProvider(rpc))
    # Stores pair as key latest data as value
    response: Dict[str, List[int]] = {}
    # AggregatorV3Interface ABI
    for pair, address in addresses.items():
        # Set up contract instance
        contract = web3.eth.contract(address=address, abi=AggregatorV3Interface)
        # Make call to latestRoundData()
        try:
            decimals = contract.functions.decimals().call()
            latestData = contract.functions.latestRoundData().call()
            response[pair] = {
                "roundId": latestData[0],
                "answer": latestData[1] / (10 ** decimals),
                "startedAt": latestData[2],
                "updatedAt": latestData[3],
                "answeredInRound": latestData[4]
            }
        except Exception as e:
            print(f"Error fetching data for {pair}: {e}")
    return JSONResponse(content=response)
