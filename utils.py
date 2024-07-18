import importlib.util

def find_spec_wrapper(name):
    return importlib.util.find_spec(name) is not None