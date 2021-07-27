#!/usr/bin/python3
import operator
import sys
import json
import os

from violas.exts import (
    jsonrpc_ext as jsonrpc,
    )

from .factory_base import (
        factory_base,
        field
        )

def parse_balances(balances):
    datas = []
    if balances:
        for balance in balances:
            datas.append({"amount": balance.amount, "currency": balance.currency})
    return datas

def parse_role(role):
    datas = {}
    if role:
        datas.update({"type": role.type})
        datas.update({"num_children": role.num_children})
        datas.update({"base_url": role.base_url})
        datas.update({"human_name": role.human_name})
        datas.update({"compliance_key": role.compliance_key})
        datas.update({"expiration_time": role.expiration_time})
    return datas
        

class account_factory(factory_base):
    account_fields = [
            ##field("tran_type",         "transaction.type"),
            field("delegated_key_rotation_capability",      "delegated_key_rotation_capability"),
            field("delegated_withdrawal_capability",        "delegated_withdrawal_capability"),
            field("received_events_key",        "received_events_key"),
            field("authentication_key",         "authentication_key"),
            field("balances",                   "balances", parse_balances),
            field("sequence_number",            "sequence_number"),
            field("sent_events_key",            "sent_events_key"),
            field("is_frozen",                  "is_frozen"),
            field("role",                       "role", parse_role),
            ]

    def __init__(self, data):
        factory_base.__init__(self, data, self.account_fields)

    def is_published(self, token_id):
        for balance in self.__data.balances:
            if token_id == balance.currency:
                return True
        return False

    def get_role_id(self):
        role_id = self.role.type
        if role_id == jsonrpc.ACCOUNT_ROLE_CHILD_VASP:
            return 6
        elif role_id == jsonrpc.ACCOUNT_ROLE_PARENT_VASP:
            return 5
        elif role_id == jsonrpc.ACCOUNT_ROLE_DESIGNATED_DEALER:
            return 2
        elif role_id == jsonrpc.ACCOUNT_ROLE_UNKNOWN:
            return sys.maxsize

        raise Exception(f"no-match role for {role_id}")

