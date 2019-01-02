#Vers 1
def longest(a1, a2):
    return "".join(sorted(set(a1 + a2)))

#Vers 2
def longest(a,b):
    a, b = sorted(list(set(a))), sorted(list(set(b)))
    result = set(a+b)
    result =sorted(list(result))
    result = ''.join(result)
    return result