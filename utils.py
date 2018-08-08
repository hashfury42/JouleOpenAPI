#!/usr/bin/python
# -*- coding: utf-8 -*-
import functools
from flask import request
from flask import jsonify
from config import VERIFY_KEY


class ExceptionHandler(object):

    def __call__(self, func):
        def _call(*args, **kwargs):
            try:
                res = func(*args, **kwargs)
                res_final = {"status": 0}
                res_final.update(res)
                return res_final
            except Exception as e:
                return {"status": -1, "err_msg": e.message}

        return _call


def verify(func):
    @functools.wraps(func)
    def call(*args, **kwargs):
        if VERIFY_KEY != request.args.get("verify_key"):
            return jsonify({"status": -1, "err_msg": "verify_key is not accepted!"})
        else:
            return func(*args, **kwargs)
    return call