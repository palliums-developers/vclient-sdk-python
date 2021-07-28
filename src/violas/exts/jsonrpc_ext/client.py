import sys
import json
import os
import typing
import requests
from logging import Logger, getLogger
from violas.data_factory import (
        transaction_factory as transaction,
        account_factory as account,
        metadata_factory as metadata,
        currency_factory as currency,
        #event_factory as event
        )

print("** this is " + __file__)

from diem import (
        diem_types,
        )

from diem.jsonrpc import (
        Client,
        Retry,
        RequestStrategy,
        Account,
        )
class VClient(Client):

    def __init__(
            self,
            server_url: str,
            session: typing.Optional[requests.Session] = None,
            timeout: typing.Optional[typing.Tuple[float, float]] = None,
            retry: typing.Optional[Retry] = None,
            rs: typing.Optional[RequestStrategy] = None,
            logger: typing.Optional[Logger] = None,
            ) -> None:
        Client.__init__(self, 
                server_url, 
                session,
                timeout,
                retry,
                rs,
                logger
                )

    
    def get_transactions(
        self,
        start_version: int,
        limit: int,
        include_events: typing.Optional[bool] = None,
        fmt: bool = True,
    ):
        """get transactions

        Returns empty list if no transactions found

        See [JSON-RPC API Doc](https://github.com/diem/diem/blob/master/json-rpc/docs/method_get_transactions.md)
        """
        datas = super().get_transactions(start_version, limit, include_events)

        if fmt:
            return [transaction(data) for data in datas]
        else:
            return [data for data in datas]

    def get_account(
        self, account_address: typing.Union[diem_types.AccountAddress, str],
        fmt: bool = True,
    ):
        datas = super().get_account(account_address)
        if fmt:
            return account(datas)
        else:
            return datas

    def to_json(self, data = None):
        return "to json"

    def get_account_transaction(
        self,
        account_address: typing.Union[diem_types.AccountAddress, str],
        sequence: int,
        include_events: typing.Optional[bool] = None,
        fmt: bool = True,
    ):
        datas = super().get_account_transaction(account_address, sequence, include_events)
        if fmt:
            return transaction(datas)
        else:
            return datas

    def get_account_transactions(
        self,
        account_address: typing.Union[diem_types.AccountAddress, str],
        sequence: int,
        limit: int,
        include_events: typing.Optional[bool] = None,
        fmt: bool = True,
    ):
        """get on-chain account transactions by start sequence number and limit size

        Returns empty list if no transactions found

        See [JSON-RPC API Doc](https://github.com/diem/diem/blob/master/json-rpc/docs/method_get_account_transactions.md)
        """

        datas = super().get_account_transactions(account_address, sequence, limit, include_events)

        if fmt:
            return [transaction(data) for data in datas]
        else:
            return [data for data in datas]

    def get_metadata(
        self,
        version: typing.Optional[int] = None,
        fmt: bool = True,
    ):
        """get block metadata

        See [JSON-RPC API Doc](https://github.com/diem/diem/blob/master/json-rpc/docs/method_get_metadata.md)
        """
        datas = super().get_metadata(version)
        if fmt:
            return metadata(datas)
        else:
            return datas

    def get_events(self, 
            event_stream_key: str, 
            start: int, 
            limit: int,
            fmt: bool = True,
    ):
        """get events

        Returns empty list if no events found

        See [JSON-RPC API Doc](https://github.com/diem/diem/blob/master/json-rpc/docs/method_get_events.md)
        """
        datas = super().get_events(event_stream_key, start, limit)
        if fmt:
            return None #[event(data) for data in datas]
        else:
            return datas


    def get_currencies(self, 
            fmt: bool = True
            ):
        """get currencies

        See [JSON-RPC API Doc](https://github.com/diem/diem/blob/master/json-rpc/docs/method_get_currencies.md)
        """

        datas = super().get_currencies()
        if fmt:
            return [currency(data) for data in datas]
        else:
            return datas



