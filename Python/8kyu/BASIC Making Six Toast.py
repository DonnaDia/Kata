#Vers 1
def six_toast(num):
    return num if num < 6 else 0 if num == 6 else num - 6


#Vers 2
def six_toast(num):
   return 6 - num if num < 6 else 0 if num == 6 else num - 6


#Vers 3
def six_toast(num):
    if num < 6:
        return num
    elif num == 6:
        return 0
    elif num > 6:
        return num - 6