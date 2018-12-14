#Version 1
def rental_car_cost(d):
    if d >= 7: return d * 40 - 50
    elif d >= 3: return d * 40 -20
    return d * 40

#Version 2
def rental_car_cost(d):
    cost = 40
    total = d * cost

    if d >= 3 and d < 7:
        total -= 20
    elif d >= 7:
        total -= 50

    return total    