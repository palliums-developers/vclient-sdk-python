import sys
import json
import os
from . import contexts
print("** this is " + __file__)
from diem import (
        diem_types,
        testnet,
        utils,
        identifier,
        )

from diem.utils import InvalidAccountAddressError, InvalidSubAddressError
from diem.auth_key import AuthKey

# keep this import for backwards compatible
from .exts import (
        jsonrpc_ext as jsonrpc,
        stdlib_ext as stdlib
        )

from .data_factory import *

from .wallet import (
        Wallet,
        LocalAccount
        )


