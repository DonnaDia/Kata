#Vers 1
def mxdiflg(a1, a2):
    if a1 and a2:
        return max(abs(len(x) - len(y)) for x in a1 for y in a2)
    return -1

#Vers 2
def mxdiflg(a1, a2):
    return str(max(len(x) for x in a1) - max(len(x) for x in a2)) if a1 and a2 else -1