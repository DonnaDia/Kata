#Vers 1
def pythagorean_triple(integers):
    middle = (integers[0] + integers[1] + integers[2]) - min(integers) - max(integers)
    return True if max(integers)**2 == (middle**2) + (min(integers)**2) else False


#Vers 2
def pythagorean_triple(integers):
    middle = (integers[0] + integers[1] + integers[2]) - min(integers) - max(integers)
    if max(integers)**2 == (middle**2) + (min(integers)**2):
        return True
    else:
        return False