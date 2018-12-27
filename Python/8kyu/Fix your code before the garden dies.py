#Vers 1
def rain_amount(mm):
    if mm < 40:
             return "You need to give your plant " + str(40 - mm) + "mm of water"
    else:
             return "Your plant has had more than enough water for today!"


#Vers 2
def rain_amount(mm):
    if mm >= 40:
        return "Your plant has had more than enough water for today!"
    elif mm > 0 and mm < 40:
        mm = 40 - mm
        return "You need to give your plant " + str(mm) + "mm of water"
    elif mm == 0:
        mm += 40 
        return "You need to give your plant " + str(mm) + "mm of water"