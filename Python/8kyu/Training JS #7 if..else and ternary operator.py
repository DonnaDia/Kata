#Vers 1
def sale_hotdogs(n):
    return n * (100 if n < 5 else 95 if n >= 5 and n < 10 else 90)


#Vers 2
def sale_hotdogs(n):
    price = 100 if n < 5 else 95 if n >= 5 and n < 10 else 90
    return price * n


#Vers 3
def sale_hotdogs(n):
    price = 0
    if n < 5:
        price = 100
    elif n >= 5 and n < 10:
        price = 95
    elif n >= 10:
        price = 90

    return price * n