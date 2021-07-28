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

class currency_factory(factory_base):

    fields = [
            field("burn_events_key"),
            field("cancel_burn_events_key"),
            field("code"),
            field("exchange_rate_update_events_key"),
            field("fractional_part"),
            field("mint_events_key"),
            field("preburn_events_key"),
            field("scaling_factor"),
            field("to_xdx_exchange_rate"),
            ]

    def __init__(self, data):
        factory_base.__init__(self, data)
        self.__init_show_fields()
    
    def __init_show_fields(self):
        self.set_fields(self.fields)


