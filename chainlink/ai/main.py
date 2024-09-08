from typing import Dict, List

from web3 import Web3

from chainlink.abi import GaladrielABI


def ask_ai(rpc: str, address: str, message: str, private_key: str) -> str:
    web3 = Web3(Web3.HTTPProvider(rpc))
    if not web3.is_connected():
        raise Exception("Failed to connect to the blockchain")
    response = ""
    caller = "0x5F240816e9F43bbD1Be924016451536F3317A02D"
    if not web3.is_address(caller) or not web3.is_address(address):
        raise Exception("Failed to connect to the blockchain")
        # Optionally, convert to a checksum address
    caller_address = web3.to_checksum_address(caller)
    contract_address = web3.to_checksum_address(address)
    print(f"Valid Ethereum address: {caller_address}")
    nonce = web3.eth.get_transaction_count(caller_address)
    contract = web3.eth.contract(address=contract_address, abi=GaladrielABI)
    try:
        transaction = contract.functions.sendMessage(message).build_transaction({
            'nonce': nonce +1,
            'gas': 200000,
            'gasPrice': web3.to_wei('20', 'gwei'),
        })
        # Sign the transaction
        signed_txn = web3.eth.account.sign_transaction(transaction, private_key=private_key)
        # Send the transaction
        txn_hash = web3.eth.send_raw_transaction(signed_txn.raw_transaction)
        res = txn_hash
        print(f"Transaction successful with hash: {txn_hash.hex()}")
    except Exception as e:
        print(f"Error while asking ai")
        res = e.__str__()
    return response


def get_response(rpc: str, address: str) -> str:
    # Change this to use your own RPC URL
    web3 = Web3(Web3.HTTPProvider(rpc))
    # Stores pair as key latest data as value
    response = ""
    contract = web3.eth.contract(address=address, abi=GaladrielABI)
    # Make call to latestRoundData()
    try:
        response = contract.functions.response().call()
    except Exception as e:
        print(f"Error while asking ai")
    return response
