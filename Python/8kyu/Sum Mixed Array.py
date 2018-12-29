#Vers 1
def sum_mix(arr):
    return sum(int(n) for n in arr)

#Vers 2
def sum_mix(arr):
    result = []
    for x in arr:
        x = int(x)
        result.append(x)
        
    return sum(result) 