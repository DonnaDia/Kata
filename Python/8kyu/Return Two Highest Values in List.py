#Vers 1
import heapq

def two_highest(arg1):
    return False if isinstance(arg1,str) else heapq.nlargest(2,set(arg1))


#Vers 2
def two_highest(arg1):
    import heapq
    for x in arg1:
        if type(x) != int:
            return False

    if arg1 == []:
        return []
    else:
        return heapq.nlargest(2,set(arg1))
