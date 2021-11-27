import conftest

from violas import (
    jsonrpc, 
    testnet, 
    transaction_factory,
    stdlib,
    )
import pytest, time

def test_get_currencies():
    client = jsonrpc.Client(testnet.JSON_RPC_URL)
    datas = client.get_currencies()
    for data in datas:
        stdlib.output(data.to_json())


test_get_currencies()

