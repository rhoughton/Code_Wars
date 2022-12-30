import sys

def total_bytes(obj): 
    return sys.getsizeof(obj)
total_bytes("hellO") 