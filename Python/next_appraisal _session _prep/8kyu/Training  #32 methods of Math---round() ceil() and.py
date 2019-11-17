#Vers 1
from math import ceil, floor

def round_it(n):
    left, right = (len(part) for part in str(n).split('.'))
    
    return ceil(n) if left < right else floor(n) if left > right else round(n)


#Vers 2
from math import ceil, floor

def round_it(n):
    check = str(n).split('.')
    
    if len(check[0]) < len(check[1]):
        return ceil(n)
    elif len(check[0]) > len(check[1]):    
        return floor(n)
    else:
        return round(n)