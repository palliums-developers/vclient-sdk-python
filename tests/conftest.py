import sys
import os

from enum import Enum

class WorkNet(Enum):
    TESTNET  = "http://testnet.diem.io"
    INTERNAL = ""
    DEVNET   = "http://124.251.110.242:8080"
    LOCAL    = "http://127.0.0.1:8080"

VIOLAS_CLIENT_SRC_DIR   = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "../src/"))

sys.path.append(VIOLAS_CLIENT_SRC_DIR)

# set worknet
node_url = WorkNet.DEVNET
print("connect to worknet: " + node_url.value)

#get node url
JSON_RPC_URL = node_url.value
