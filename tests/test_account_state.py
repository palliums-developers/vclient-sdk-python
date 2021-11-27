from conftest import *

import pytest, time

def test_account():
    client = jsonrpc.Client(testnet.JSON_RPC_URL)
    #print(jsonrpc.NetworkError)
    #stdlib.output(client.get_account_state_with_proof(testnet.DESIGNATED_DEALER_ADDRESS))
    datas = client.get_account_state_with_proof(LOCAL_ACCOUNT_ADDRESS)
    stdlib.output(client.get_account_state_with_proof(LOCAL_ACCOUNT_ADDRESS))

    stdlib.output("start deserialize........***********")
    blob_deserialize(datas.blob)

def blob_deserialize(data):
    print(type(data))
    de = bcs.BcsDeserializer(bytes.fromhex(data))
    length = de.deserialize_len()
    print(length)
    for i in range(length):
        try:
            obj_type = de.deserialize_any(violas_types.ModuleId)
            stdlib.output("find script------------------>")
            stdlib.output(obj_type)
        except Exception as e:
            pass

    
test_account()
