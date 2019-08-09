#Vers.1
def summation(num):
    sum = 0
    for i in range(1, num + 1):
        sum += i
    return sum

#Vers.2
def summation(num):
    sum = 0
    for i in range(1, num + 1): sum += i
    return sum

#Vers.3
def summation(num):
    return sum(xrange(num + 1))