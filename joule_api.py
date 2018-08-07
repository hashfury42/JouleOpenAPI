#!/usr/bin/python
# -*- coding: utf-8 -*-
from bitcoinrpc.authproxy import AuthServiceProxy, JSONRPCException
import logging
from utils import ExceptionHandler

# logging.basicConfig()
# logging.getLogger("BitcoinRPC").setLevel(logging.DEBUG)


class JouleRPC(object):
    def __init__(self):
        """
        pip install python-bitcoinrpc
        """
        self.__rpc_user = "joulecoinrpc"
        self.__rpc_password = "Cav3vsnBvZDqpL4c8QRUeuwbJq1D5txZaZkxGx8hf2gF"
        self.__rpc_connection = AuthServiceProxy("http://%s:%s@127.0.0.1:8755" % (self.__rpc_user, self.__rpc_password))

    def set_rpc_user(self, user):
        self.__rpc_user = user

    def set_rpc_password(self, password):
        self.__rpc_password = password

    def build_connection(self):
        self.__rpc_connection = AuthServiceProxy("http://%s:%s@127.0.0.1:8755" % (self.__rpc_user, self.__rpc_password))

    def get_mininginfo(self):
        self.build_connection()
        mininginfo = self.__rpc_connection.getmininginfo()
        return mininginfo

    def listaccounts(self):
        self.build_connection()
        accounts = self.__rpc_connection.listaccounts()
        return accounts

    def getreceivedbyaddress(self, address):
        self.build_connection()
        receivedbyaddress = self.__rpc_connection.getreceivedbyaddress(address)
        return receivedbyaddress

    def getnewaddress(self, account):
        self.build_connection()
        new_address = self.__rpc_connection.getnewaddress(account)
        return new_address

    def getaddressesbyaccount(self, account):
        self.build_connection()
        address = self.__rpc_connection.getaddressesbyaccount(account)
        return address

    def getinfo(self):
        self.build_connection()
        info = self.__rpc_connection.getinfo()
        return info

    def get_best_block(self):
        self.build_connection()
        best_block_hash = self.__rpc_connection.getbestblockhash()
        best_block_info = self.__rpc_connection.getblock(best_block_hash)
        return best_block_info

    def sendtoaddress(self, joulecoinaddress, amount):
        self.build_connection()
        self.__rpc_connection.walletpassphrase("000000", 60)
        tx_id = self.__rpc_connection.sendtoaddress(joulecoinaddress, amount)
        return tx_id

    @ExceptionHandler()
    def gettransaction(self, tx_id):
        tx_info = self.__rpc_connection.gettransaction(tx_id)
        return tx_info

    def create_new_account(self, account_name):
        address = self.__rpc_connection.getaccountaddress(account_name)
        return address


if __name__ == '__main__':

    # JLSj8mDh1EvTwNuDqvmKJXoB62oWgXpXJy

    joule_rpc = JouleRPC()

    # mininginfo = joule_rpc.get_mininginfo()
    # print(mininginfo)
    #
    # best_block_info = joule_rpc.get_best_block()
    # print(best_block_info)
    #
    # address = joule_rpc.getaddressesbyaccount("main")
    # print(address)
    #
    # try:
    #     res = joule_rpc.sendtoaddress("JLSj8mDh1EvTwNuDqvmKJXoB62oWgXpXJy", 1.0)
    #     print(res)
    # except Exception as e:
    #     print e.message

    print joule_rpc.gettransaction("-1")