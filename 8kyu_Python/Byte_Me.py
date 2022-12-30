'''
Return the size of an object in bytes. 
Only the memory consumption directly attributed to the object is accounted for, not the memory consumption of objects it refers to.
getsizeof() calls the objects __sizeof__ method and adds an additional garbage collector overhead if the object is managed by the garbage collector.
'''

import sys

def total_bytes(obj): 
    return sys.getsizeof(obj)
total_bytes("hellO") 