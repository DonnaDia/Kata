#Vers 1
def between(a,b):
    return range(a, b + 1)


#Vers 2
def between(a,b):
    return [x for x in range(a,b+1)]


#Vers 3
def between(a,b):
    for nums in range(a, b + 1):
        return nums