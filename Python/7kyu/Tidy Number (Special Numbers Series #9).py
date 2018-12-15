#Vers1
def tidyNumber(n):
    nlist = list(str(n))
    return nlist == sorted(nlist)

#Vers2
def tidyNumber(n):
    n = str(n)
    nlist = []
    for elem in n:
        nlist.append(elem)

    snlist = sorted(nlist)
    return True if nlist == snlist else False
        
#Vers3
def tidyNumber(n):
    n = str(n)
    nlist = []
    for elem in n:
        nlist.append(elem)

    snlist = sorted(nlist)
    if nlist == snlist:
        return True
    else:
        return False