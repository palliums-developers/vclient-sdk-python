import os
from dataclasses import dataclass, field
from typing import Dict, Optional, Tuple, Union
from mnemonic import Mnemonic
from .key_factory import KeyFactory

from diem.testing import LocalAccount

@dataclass
class Account(LocalAccount):
    address_hex: str = None
    @property
    def address(self) -> str:
        if self.address_hex:
            return self.address_hex
        else:
            return self.account_address.to_hex();

    @address.setter
    def address(self, value):
        self.address_hex = value

    @staticmethod
    def from_private_key_hex(key: str) -> "Account":
        return Account.from_dict_ex({"private_key": key})

    @staticmethod
    def from_dict_ex(dic: Dict[str, str]) -> "Account":
        lac: LocalAccount = LocalAccount.from_dict(dic)

        return Account(lac.private_key, 
                lac.compliance_key,
                lac.hrp,
                lac.txn_gas_currency_code,
                lac.txn_max_gas_amount,
                lac.txn_gas_unit_price,
                lac.txn_expire_duration_secs
                )

