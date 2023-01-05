import os
import json
from glob import glob
from types import SimpleNamespace

from functools import singledispatch
from types import SimpleNamespace

def json2obj(json_str):
    """
    Converts a json string into a python object.
    @param json_str: Contains a valid json string. Boolean values
    must be single (or double) quoted strings.
    @return: An object that can be navigated natively.
    For example, if
    x = json2obj('{"a":{"b":1}}')
    the output of print(x.a.b) will be 1.
    """
    space = {}
    for key, value in json_str.items():
#        if isinstance(value, dict):
#            value = json2obj(value)
        if key == "crops":
            if isinstance(value, dict):
                value = json2obj(value)
        space[key] = value
    return SimpleNamespace(**space)

