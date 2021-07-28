import sys
import os

VIOLAS_CLIENT_SRC_DIR   = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "../src/"))

sys.path.append(VIOLAS_CLIENT_SRC_DIR)

JSON_RPC_URL = "http://47.93.114.230:50001"
