#!/usr/bin/python
# -*- coding: utf-8 -*-


def handle_exception(func):
    def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                return e.message
    return wrapper


@handle_exception
def func():
    return 1


print func()


class tracer:

    def __init__(self, func):
        self.calls = 0
        self.func = func

    def __call__(self, *args):
        self.calls += 1
        print('call %s to %s' % (self.calls, self.func.__name__))
        self.func(*args)


@tracer
def spam(a, b, c):
    print(a + b + c)


spam(1, 2, 3)
spam(1, 2, 3)


class Foo(object):
    def __init__(self):
        pass

    def __call__(self, func):
        def _call(*args, **kw):
            print 'class decorator runing'
            return func(*args, **kw)

        return _call


class Bar(object):
    @Foo()
    def bar(self, test, ids):
        print test, ids

class ExceptionHandler(object):

    def __call__(self, func):
        def _call(*args, **kw):
            try:
                return func(*args, **kw)
            except Exception as e:
                return e.message
        return _call



Bar().bar('aa', 'ids')
