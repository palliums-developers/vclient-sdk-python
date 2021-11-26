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
    datas = client.get_metadata()
    version = datas.version
    stdlib.output(version)

    #print(jsonrpc.NetworkError)
    stdlib.output(client.get_state_proof(version))

test_account()
