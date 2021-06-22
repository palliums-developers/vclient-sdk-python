import sys
import json
import os
sys.path.append(os.getcwd())
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../lbdiemclient/src/")))
from diem import (
    diem_types,
    stdlib,
    testnet,
    utils,
    identifier,
)

from diem.utils import InvalidAccountAddressError, InvalidSubAddressError
from diem.auth_key import AuthKey

# keep this import for backwards compatible
from diem.testing import LocalAccount

from .exts import jsonrpc_ext as jsonrpc
print("** this is " + __file__)
