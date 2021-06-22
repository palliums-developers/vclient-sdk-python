import sys
import json
import os
sys.path.append(os.getcwd())
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), "../src/"))

from violas import jsonrpc, testnet
import pytest, time

def test_invalid_server_url():
    print(testnet.JSON_RPC_URL)
    client = jsonrpc.Client(testnet.JSON_RPC_URL)
    #print(jsonrpc.NetworkError)
    print(client.get_currencies())

test_invalid_server_url()
