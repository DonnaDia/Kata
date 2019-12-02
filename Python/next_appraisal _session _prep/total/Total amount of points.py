#Vers 1
def points(games):
    total = 0

    for game in games:
        result = game.split(":")

        if result[0] > result[1]:
            total += 3
        elif result[0] < result[1]:
            total += 0
        else:
            total += 1


    return total

    
#Vers 2
def points(games):
    total = 0

    x_values = [num.split(":")[0] for num in games]
    y_values = [num.split(":")[1] for num in games]

    for x, y in zip(x_values, y_values):
        if x > y:
            total += 3
        elif x < y:
            total += 0
        else:
            total += 1

    return total