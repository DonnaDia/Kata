#Vers 1
def merge_arrays(first, second): 
    return sorted(set(first + second))


#Vers 2
def merge_arrays(first, second): 
    return sorted(list(set(first+second)))