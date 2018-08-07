#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import time
import json
import random
from flask import jsonify
from flask import Flask, render_template, request
from joule_api import JouleRPC

JOULE_RPC_MODE = 0

app = Flask(__name__)
app.config['SECRET_KEY'] = "d3Rf3l0q34dGfeeTJkleNmmljeklFertReG"


@app.route('/get_mining_info')
def get_mining_info():
    joule_rpc = JouleRPC()
    mining_info = joule_rpc.get_mininginfo()
    mining_info["difficulty"] = float(mining_info["difficulty"])
    return jsonify(mining_info)


@app.route('/get_best_block')
def get_best_block():
    joule_rpc = JouleRPC()
    best_block = joule_rpc.get_best_block()
    res = {
        "height": best_block["height"],
        "difficulty": float(best_block["difficulty"]),
        "time": time.strftime("%Y/%m/%d %H:%M:%S", time.localtime(best_block["time"])),
        "hash": best_block["hash"]
    }
    return jsonify(res)


if __name__ == '__main__':

    port = 8000

    if len(sys.argv) > 1:
        port = int(sys.argv[1])
        rpc_mode = int(sys.argv[2])
        JOULE_RPC_MODE = rpc_mode
        app.run(host='0.0.0.0', port=port, threaded=True)
    else:
        app.run(host='127.0.0.1', port=port, debug=True)
