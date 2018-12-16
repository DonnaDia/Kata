#Vers1
def multi(l_st):
    mult = 1
    for elem in l_st:
        mult *= elem
    return mult
def add(l_st):
    return sum(l_st)
def reverse(string):
    return string[::-1]

#Vers 2
from numpy import sum as add, prod as multi
reverse = lambda s: s[::-1]

#Vers3
def multi(l_st):
    mult = 1
    for elem in l_st:
        mult *= elem
    return mult
def add(l_st):
    result = 0
    for elem in l_st:
        result += elem
    return result
def reverse(string):
    return string[::-1]