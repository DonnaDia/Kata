#Vers 1
from calendar import isleap as isLeapYear

#Vers 2
def isLeapYear(year):
    return (year % 100 != 0 and year % 4 == 0) or year % 400 == 0

#Vers 3
def isLeapYear(year):
    if str(year)[-2:] != '00' and year % 4 == 0:
        return True
    elif str(year)[-2:] == '00' and year % 400 == 0:
        return True
    else:
        return False

#Vers 4
def isLeapYear(year):
    return True if str(year)[-2:] != '00' and year % 4 == 0 else True if str(year)[-2:] == '00' and year % 400 == 0 \
    else False