#Vers 1
def count_by(x, n):
    return [num * x for num in range(1, n + 1)]

    
#Vers 2
def count_by(x, n):
    # range(start, stop, step)
    return range(x, x * n + 1, x)
    
    
#Vers 3
def count_by(x, n):
    return [x * num for num in range(1,n+1)]