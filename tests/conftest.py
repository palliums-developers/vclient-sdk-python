import sys
import os

from enum import Enum

VIOLAS_CLIENT_SRC_DIR   = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "../src/"))
sys.path.append(VIOLAS_CLIENT_SRC_DIR)

from violas import (
    jsonrpc, 
    testnet, 
    transaction_factory,
    stdlib,
    bcs,
    violas_types,
    )

class WorkNet(Enum):
    TESTNET  = "http://testnet.diem.io"
    INTERNAL = ""
    DEVNET   = "http://124.251.110.242:8080"
    LOCAL    = "http://127.0.0.1:8080"


# set worknet
node_url = WorkNet.DEVNET

#redirect node json rpc url 
testnet.JSON_RPC_URL = node_url.value

LOCAL_ACCOUNT_ADDRESS = "249BDDDE5A2ECA70515FB25B2CA07A11"

print("------> connect to: " + testnet.JSON_RPC_URL)
