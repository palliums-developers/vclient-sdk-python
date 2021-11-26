from conftest import *

import pytest, time

def test_account():
    client = jsonrpc.Client(testnet.JSON_RPC_URL)
    #print(jsonrpc.NetworkError)
    #stdlib.output(client.get_account(testnet.DESIGNATED_DEALER_ADDRESS, fmt = False))
    stdlib.output(client.get_account(LOCAL_ACCOUNT_ADDRESS, fmt = False))

test_account()
