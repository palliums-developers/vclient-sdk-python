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

from .event_factory import (
        event_factory,
    )

def parse_events(events):
    datas = []
    if events:
        for event in events:
            datas.append(event_factory(event).to_json())
            #datas.append({
            #    "key":event.key,
            #    "sequence_number": event.sequence_number,
            #    "transaction_version":event.transaction_version,
            #    "data": {
            #        "type": event.data.type,
            #        "amount": {
            #            "amount": event.data.amount.amount,
            #            "currency": event.data.amount.currency,
            #            },
            #        "sender" : event.data.sender,
            #        "receiver": event.data.receiver,
            #        }
            #    })
    return datas


def parse_state(state):
    return state == "executed"

class transaction_factory(factory_base):

    global parse_state
    tran_fields = [
            field("events",             "events", parse_events),
            field("gas_used",           "gas_used"),
            field("hash",               "hash"),
            field("version",            "version"),
            field("sender",             "transaction.sender"),
            field("sequence_number",    "transaction.sequence_number"),
            field("type",               "transaction.type"),
            field("chain_id",           "transaction.chain_id"),
            field("expiration_timestamp_secs",          "transaction.expiration_timestamp_secs"),
            field("gas_currency",       "transaction.gas_currency"),
            field("gas_unit_price",     "transaction.gas_unit_price"),
            field("max_gas_amount",     "transaction.max_gas_amount"),
            field("public_key",         "transaction.public_key"),
            field("signature",          "transaction.signature"),
            field("signature_scheme",   "transaction.signature_scheme"),
            field("script_hash",        "transaction.script_hash"),

            field("script_type",        "transaction.script.type"),
            field("currency",           "transaction.script.currency"),
            field("amount",             "transaction.script.amount"),
            field("metadata",           "transaction.script.metadata"),
            field("metadata_signature", "transaction.script.metadata_signature"),
            field("receiver",           "transaction.script.receiver"),
            field("state",              "vm_status.type", parse_state),
            field("vm_status",          "vm_status.type"),
            ]

    def __init__(self, data):
        factory_base.__init__(self, data)
        self.__init_show_fields()

    def __init_show_fields(self):
        self.set_fields(self.tran_fields)

        default_outputs = {"state": "not support",
                "events_len" : len(self.events)}

        self.extend_default_outputs(default_outputs)


    def get_version(self):
        return self.get_attr_with_path(self.get_field("version").path)

