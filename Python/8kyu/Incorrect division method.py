#Vers.1
from __future__ import division

def divide_numbers(x,y):
    return x // y if x % y == 0 else x / y

#Vers.2
def divide_numbers(x,y):
    return x / y if x % y == 0 else float(x) / float(y)