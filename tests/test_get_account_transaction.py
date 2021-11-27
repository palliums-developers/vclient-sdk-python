import conftest

from violas import (
    jsonrpc, 
    testnet, 
    transaction_factory,
    stdlib,
    )
import pytest, time

def test_get_account_transaction():
    client = jsonrpc.Client(testnet.JSON_RPC_URL)
    transaction = client.get_account_transaction(testnet.DESIGNATED_DEALER_ADDRESS, 10, True, False)
    stdlib.output(transaction)

test_get_account_transaction()
