# First, install ipdb and/or pdbpp:
#
# python3 -m pip install ipdb pdbpp
# 
# To use pdbpp, no extra steps required! Keep going with normal pdb syntax.
# For ipdb, import the module:
# import ipdb
# Then add `ipdb.set_trace()` wherever you want a breakpoint.
import pdb

def mult(a, b):
    print(f"multiplying {a} and {b}")
    return a * b

def add(a, b):
    print(f"adding {a} and {b}")
    return a + b

result = 0

result = mult(3, 5)
result = add(result, 10) 
result = mult(result, 4) 
result = add(result, 13) 
print(result)

