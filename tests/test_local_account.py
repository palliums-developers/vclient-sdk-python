import sys
import conftest 
import pytest, time
from violas import (
    jsonrpc, 
    testnet,
    LocalAccount,
    identifier,
    utils,
        )

def __show_info(info):
    print("{}:{}".format(sys._getframe(1).f_code.co_name, info))

def test_from_private_key_hex():
    account = LocalAccount.generate()
    hex_key = utils.private_key_bytes(account.private_key).hex()
    new_account = LocalAccount.from_private_key_hex(hex_key)
    assert utils.private_key_bytes(new_account.private_key).hex() == hex_key
    __show_info(hex_key);

test_from_private_key_hex();

def test_from_and_to_dict():
    config = {
        "private_key": "ab70ae3aa603641f049a3356927d0ba836f775e862f559073a6281782479fd1e",
        "compliance_key": "f75b74a94250bda7abfab2045205e05c56e5dcba24ecea6aff75aac9463cdc2f",
        "hrp": "tdm",
        "txn_gas_currency_code": "XDX",
        "txn_max_gas_amount": 1000000,
        "txn_gas_unit_price": 0,
        "txn_expire_duration_secs": 30,
    }
    account = LocalAccount.from_dict(config)
    assert account.to_dict() == config
    __show_info(config);

test_from_and_to_dict()

def test_generate_keys():
    account = LocalAccount.generate()
    sig1 = account.private_key.sign(b"test")
    sig2 = account.compliance_key.sign(b"test")

    load_account = LocalAccount.from_dict(account.to_dict())
    assert sig1 == load_account.private_key.sign(b"test")
    assert sig2 == load_account.compliance_key.sign(b"test")
    __show_info("sig1={} \r\nsig2={}".format(sig1.hex(), sig2.hex()));

test_generate_keys()
