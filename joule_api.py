#!/usr/bin/python
# -*- coding: utf-8 -*-
from bitcoinrpc.authproxy import AuthServiceProxy, JSONRPCException
from utils import ExceptionHandler

import logging


# logging.basicConfig()
# logging.getLogger("BitcoinRPC").setLevel(logging.DEBUG)


class JouleRPC(object):
    def __init__(self):
        """
        pip install python-bitcoinrpc
        """
        self.__rpc_user = ""
        self.__rpc_password = ""
        self.__rpc_connection = AuthServiceProxy("http://%s:%s@127.0.0.1:8755" % (self.__rpc_user, self.__rpc_password))

    def set_rpc_user(self, user):
        self.__rpc_user = user

    def set_rpc_password(self, password):
        self.__rpc_password = password

    def build_connection(self):
        self.__rpc_connection = AuthServiceProxy("http://%s:%s@127.0.0.1:8755" % (self.__rpc_user, self.__rpc_password))

    @ExceptionHandler()
    def get_mining_info(self):
        self.build_connection()
        mininginfo = self.__rpc_connection.getmininginfo()
        return {"mininginfo": mininginfo}

    @ExceptionHandler()
    def list_accounts(self):
        self.build_connection()
        accounts = self.__rpc_connection.listaccounts()
        for k,v in accounts.items():
            accounts[k] = float(v)
        return {"accounts": accounts}

    @ExceptionHandler()
    def get_received_by_address(self, address):
        self.build_connection()
        receivedbyaddress = self.__rpc_connection.getreceivedbyaddress(address)
        return {"receivedbyaddress": receivedbyaddress}

    @ExceptionHandler()
    def get_new_address(self, account):
        self.build_connection()
        new_address = self.__rpc_connection.getnewaddress(account)
        return {"new_address": new_address}

    @ExceptionHandler()
    def get_addresses_by_account(self, account):
        self.build_connection()
        address = self.__rpc_connection.getaddressesbyaccount(account)
        return {"address": address}

    @ExceptionHandler()
    def get_info(self):
        self.build_connection()
        info = self.__rpc_connection.getinfo()
        info_final = {
            "blocks": info["blocks"],
            "difficulty": float(info["difficulty"]),
            "balance": float(info["balance"])
        }
        return {"info": info_final}

    @ExceptionHandler()
    def get_best_block(self):
        self.build_connection()
        best_block_hash = self.__rpc_connection.getbestblockhash()
        best_block_info = self.__rpc_connection.getblock(best_block_hash)
        return {"best_block_info": best_block_info}

    @ExceptionHandler()
    def send_to_address(self, address, amount):
        self.build_connection()
        # self.__rpc_connection.walletpassphrase("000000", 6000)
        tx_id = self.__rpc_connection.sendtoaddress(address, amount)
        return {"tx_id": tx_id}

    @ExceptionHandler()
    def get_transaction(self, tx_id):
        self.build_connection()
        tx_info = self.__rpc_connection.gettransaction(tx_id)
        return {"tx_info": tx_info}

    @ExceptionHandler()
    def create_new_account(self, account_name):
        self.build_connection()
        address = self.__rpc_connection.getaccountaddress(account_name)
        return {"address": address, "account": account_name}


if __name__ == '__main__':
    # JLSj8mDh1EvTwNuDqvmKJXoB62oWgXpXJy

    joule_rpc = JouleRPC()

    # 获取目前挖矿信息
    mininginfo = joule_rpc.get_mining_info()
    print(mininginfo)

    # 获取最新区块信息
    best_block_info = joule_rpc.get_best_block()
    print(best_block_info)

    # 获取账号下面的新地址
    address = joule_rpc.get_new_address("main")
    print(address)

    # 获取交易信息
    tx_info = joule_rpc.get_transaction("13043c0a2ca6827d2c8b0e548b7a07a5dc56dfbe57d50cb158b2e4f5928536ea")
    print(tx_info)

    # 创建新账户
    # account = joule_rpc.create_new_account("blank2")
    # print(account)

    # 向某个地址转账
    tx_id = joule_rpc.send_to_address("JLSj8mDh1EvTwNuDqvmKJXoB62oWgXpXJy", 1)
    print(tx_id)

    # 获取最新账户信息
    info = joule_rpc.get_info()
    print(info)

    # 获取各个账户下面的余额信息
    account_info = joule_rpc.list_accounts()
    print(account_info)



