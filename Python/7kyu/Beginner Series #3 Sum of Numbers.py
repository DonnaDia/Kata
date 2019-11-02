#Vers 1
def get_sum(a,b):
    return sum(range(min(a,b), max(a,b) + 1))

#Vers 2
def get_sum(a,b):     
    if a > b:
        return sum([i for i in range(b,a + 1)])
    elif b > a:
        return sum([i for i in range(a,b + 1)])
    else:
        return a