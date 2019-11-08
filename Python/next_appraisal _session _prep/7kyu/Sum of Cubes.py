#Vers 1
def sum_cubes(n):
    return sum(i**3 for i in range(1, n+1))

#Vrs 2
def sum_cubes(n):
    return sum([i**3 for i in range(1, n+1)]) 