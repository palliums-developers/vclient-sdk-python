import conftest

import pytest, time
from violas import (
    jsonrpc, 
    testnet, 
    transaction_factory,
    stdlib,
    )

def test_account():
    client = jsonrpc.Client(testnet.JSON_RPC_URL)
    #print(jsonrpc.NetworkError)
    stdlib.output(client.get_account_state_with_proof(testnet.DESIGNATED_DEALER_ADDRESS).to_json())

test_account()
