import conftest

from violas import (
    jsonrpc, 
    testnet, 
    transaction_factory,
    stdlib,
    )
import pytest, time

def test_get_metadata():
    client = jsonrpc.Client(testnet.JSON_RPC_URL)
    datas = client.get_metadata(1000000)
    stdlib.output(datas.to_json())


test_get_metadata()
