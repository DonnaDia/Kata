#Vers 1
def find_short(s):
    return min(map(len,s.split(' ')))

#Vers 2
find_short = lambda s: min(len(e) for e in s.split())

#Vers 3
def find_short(s):
    return min(len(x) for x in s.split())

#Vers 4
def find_short(s):
    s = s.split(' ')
    n = []
    for el in s:
        n.append(len(el))

    return min(n)