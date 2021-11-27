import conftest

from violas import (
    jsonrpc, 
    testnet, 
    transaction_factory,
    stdlib,
    )
import pytest, time

def test_get_transactions():
    client = jsonrpc.Client(testnet.JSON_RPC_URL)
    transactions = client.get_transactions(1000, 1, True)
    for transaction in transactions:
        stdlib.output(transaction.to_json())

def test_get_account_state_with_proof():
    client = jsonrpc.Client(conftest.JSON_RPC_URL)
    #state_proof = client.get_account_state_with_proof(testnet.DESIGNATED_DEALER_ADDRESS)
    state_proof = client.get_account_state_with_proof("00000000000000000042524746554e44")
    assert state_proof is not None
    assert isinstance(state_proof, jsonrpc.AccountStateWithProof)
    assert state_proof.version == client.get_last_known_state().version
    print(state_proof)

#test_get_account_state_with_proof()
test_get_transactions()
