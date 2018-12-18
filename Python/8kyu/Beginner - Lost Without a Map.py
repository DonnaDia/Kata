#Vers1
def maps(a):
    b = [elem * 2 for elem in a]
    return b

print(maps([1, 2, 3]))

#Vers2
def maps(a):
    def map_func(a):
        b = [elem * 2 for elem in a]
        return b
    return map_func(a)

print(maps([1, 2, 3]))