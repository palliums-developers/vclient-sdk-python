import conftest

from violas import jsonrpc, testnet, transaction_factory
import pytest, time

def test_get_transactions():
    client = jsonrpc.Client(testnet.JSON_RPC_URL)
    transactions = client.get_transactions(1000000, 1, True)
    for transaction in transactions:
        print(transaction_factory(transaction).to_json())

