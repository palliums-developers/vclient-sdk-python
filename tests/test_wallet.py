
import sys
import json
import os
sys.path.append(os.getcwd())
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), "../src/"))

from violas import (
        Wallet
        )
import pytest, time

def show_msg(msg):
    print(msg)

def test_new_account():
    wallet = Wallet.new()
    wallet.new_account()
    wallet.new_account()
    show_msg("account count:{} ".format(wallet.child_number))
    for account in wallet.accounts:
        print("account address: " + account.address)


test_new_account()
