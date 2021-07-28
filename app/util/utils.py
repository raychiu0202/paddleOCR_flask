import numpy as np


def hasNone(*args):
    for arg in args:
        if arg is None:
            return True
    return False


def isEmpty(c):
    return c is None or len(c) == 0
