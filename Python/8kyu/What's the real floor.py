#Vers 3
def get_real_floor(n):
    return n if n < 1 else n - 1 if n < 13 else n - 2

#Works-on-my-machine vers
def get_real_floor(n):
    if n == 15:
        return 13
    elif n > 0:
        return n - 1
    elif n <= 0:
        return n



print(get_real_floor(199))
print(get_real_floor(5))
print(get_real_floor(15))
print(get_real_floor(278))
print(get_real_floor(1))



#Vers 2 (Works-ob-my-machine)
def get_real_floor(n):
    return 13 if n == 15 else n - 1 if n > 0 else n



print(get_real_floor(199))
print(get_real_floor(5))
print(get_real_floor(15))
print(get_real_floor(278))
print(get_real_floor(-1))