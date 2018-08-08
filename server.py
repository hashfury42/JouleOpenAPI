#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import time
import json
import random
import config
from flask import jsonify
from flask import Flask, render_template, request
from joule_api import JouleRPC
from utils import verify


app = Flask(__name__)
app.config['SECRET_KEY'] = "d3Rf3l0q34dGfeeTJkleNmmljeklFertReG"


joule_rpc = JouleRPC()
joule_rpc.set_rpc_user(config.RPC_USER)
joule_rpc.set_rpc_password(config.RPC_PASSWD)


@app.route("/get_mining_info")
@verify
def get_mining_info():
    mining_info = joule_rpc.get_mining_info()
    return jsonify(mining_info)


@app.route("/get_received_by_address")
@verify
def get_received_by_address():
    receivedbyaddress = joule_rpc.get_received_by_address(request.args["address"])
    return jsonify(receivedbyaddress)


@app.route("/list_accounts")
@verify
def list_accounts():
    accounts = joule_rpc.list_accounts()
    return jsonify(accounts)


@app.route("/get_info")
@verify
def get_info():
    info = joule_rpc.get_info()
    return jsonify(info)


@app.route("/get_best_block")
@verify
def get_best_block():
    best_block = joule_rpc.get_best_block()
    return jsonify(best_block)


@app.route("/send_to_address")
@verify
def send_to_address():
    tx_id = joule_rpc.send_to_address(request.args["address"], float(request.args["amount"]))
    return jsonify(tx_id)


@app.route("/get_transaction")
@verify
def get_transaction():
    tx = joule_rpc.get_transaction(request.args["tx_id"])
    return jsonify(tx)


@app.route("/create_new_account")
@verify
def create_new_account():
    account = joule_rpc.create_new_account(request.args["account_name"])
    return jsonify(account)


@app.route("/get_addresses_by_account")
@verify
def get_addresses_by_account():
    addresses = joule_rpc.get_addresses_by_account(request.args["account_name"])
    return jsonify(addresses)


@app.route("/get_new_address")
@verify
def get_new_address():
    address = joule_rpc.get_new_address(request.args["account_name"])
    return jsonify(address)


if __name__ == '__main__':

    port = 8000
    app.run(host="127.0.0.1", port=port, threaded=True)

