from typing import Dict, List

from web3 import Web3

from chainlink.abi import AggregatorV3Interface


def get_price(rpc: str, addresses: Dict[str, str]) -> Dict[str, List[int]]:
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
            latestData = contract.functions.latestRoundData().call()
            response[pair] = latestData
        except:
            pass
            # TODO log the error
    return response
