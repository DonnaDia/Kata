#Vers1
def problem(a):
    return 'Error' if type(a) == str else a * 50 + 6

#Vers2
def problem(a):
    if type(a) == str:
        return 'Error'
    else:
        return a * 50 + 6