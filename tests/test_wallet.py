import conftest 

from violas import (
        Wallet
        )
import pytest, time

vwallet = "vwallet"
def show_msg(msg):
    print(msg)

def test_new_account():
    wallet = Wallet.new()
    wallet.new_account()
    wallet.new_account()
    show_msg("account count:{} ".format(wallet.child_number))
    for account in wallet.accounts:
        print("account address: " + account.address)

def test_load_from_file():
    wallet = Wallet.recover(vwallet)
    show_msg("account count:{} ".format(wallet.child_number))
    for account in wallet.accounts:
        print(f'''
        address:    {account.address}
        auth_key:   {account.auth_key.hex()[:32]}
        publickey:  {account.public_key_bytes.hex()}
        identifier: {account.account_identifier()}
        hrp:        {account.hrp}

        '''
        )

def test_load_from_file_list():
    wallet = Wallet.recover(vwallet)
    show_msg("account count:{} ".format(wallet.child_number))
    for account in wallet.accounts:
        print(f''' address:    {account.address} ''')

test_load_from_file_list()
