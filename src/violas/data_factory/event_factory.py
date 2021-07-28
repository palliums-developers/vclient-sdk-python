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

def parse_amount(amount):
    datas = {}
    if amount:
        datas.update({"amount":amount.amount, "currency": amount.currency})
    return datas

class data_factory(factory_base):

    fields = [
            field("type"),
            field("amount", "amount", parse_amount),
            field("preburn_address"),
            field("currency_code"),
            field("new_to_xdx_exchange_rate"),
            field("sender"),
            field("receiver"),
            field("metadata"),
            field("new_compliance_public_key"),
            field("time_rotated_seconds"),
            field("new_base_url"),
            field("committed_timestamp_secs"),
            field("epoch"),
            field("round"),
            field("proposer"),
            field("proposed_time"),
            field("destination_address"),
            field("created_address"),
            field("role_id"),
            field("address"),
            field("domain"),
            field("removed"),
            field("bytes", "bytes"),
            ]

    def __init__(self, data):
        factory_base.__init__(self, data)
        self.__init_show_fields()
    
    def __init_show_fields(self):
        self.set_fields(self.fields)

def parse_data(data):
    return data_factory(data).to_json()

class event_factory(factory_base):

    fields = [
            field("key"),
            field("sequence_number"),
            field("transaction_version"),
            field("data", "data", parse_data),
            ]

    def __init__(self, data):
        factory_base.__init__(self, data)
        self.__init_show_fields()
    
    def __init_show_fields(self):
        self.set_fields(self.fields)


