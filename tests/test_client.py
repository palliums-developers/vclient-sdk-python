import conftest

from violas import jsonrpc, testnet
import pytest, time

def test_invalid_server_url():
    print(testnet.JSON_RPC_URL)
    client = jsonrpc.Client(testnet.JSON_RPC_URL)
    #print(jsonrpc.NetworkError)
    print(client.get_currencies())
    print(client.to_json())

test_invalid_server_url()
