#Vers 1
def whatday(num):
    days = ('Sun', 'Mon', 'Tues', 'Wednes', 'Thurs', 'Fri', 'Satur')
    return days[num-1] + 'day' if 0 < num < 8 else 'Wrong, please enter a number between 1 and 7' 


#Vers 2
def whatday(num):
    return 'Sunday' if num == 1 else 'Monday' if num == 2 else 'Tuesday' if num == 3 \
    else 'Wednesday' if num == 4 else 'Thursday' if num == 5 else 'Friday' if num == 6 else 'Saturday' \
    if num == 7 else 'Wrong, please enter a number between 1 and 7'