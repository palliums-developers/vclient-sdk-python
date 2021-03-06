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

class metadata_factory(factory_base):

    fields = [
            field("version"),
            field("timestamp"),
            field("chain_id"),
            field("diem_version"),
            field("accumulator_root_hash"),
            field("dual_attestation_limit"),
            field("script_hash_allow_list", callback = factory_base.parse_list),
            field("module_publishing_allowed"),
            ]

    def __init__(self, data):
        factory_base.__init__(self, data)
        self.__init_show_fields()
    
    def __init_show_fields(self):
        self.set_fields(self.fields)

