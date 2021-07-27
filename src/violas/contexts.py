import sys
import os

DIEM_CLIENT_SRC_DIR     = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), f"../../lbdiemclient/src/"))
VIOLAS_CLIENT_SRC_DIR   = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "../"))

sys.path.append(DIEM_CLIENT_SRC_DIR)
sys.path.append(VIOLAS_CLIENT_SRC_DIR)

