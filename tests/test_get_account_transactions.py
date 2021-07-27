import conftest

from violas import (
    jsonrpc, 
    testnet, 
    transaction_factory,
    stdlib,
    )
import pytest, time

def test_get_account_transactions():
    client = jsonrpc.Client(testnet.JSON_RPC_URL)
    transactions = client.get_account_transactions(testnet.DESIGNATED_DEALER_ADDRESS, 1, 10, True)
    for transaction in transactions:
        stdlib.output(transaction.to_json())

test_get_account_transactions()
