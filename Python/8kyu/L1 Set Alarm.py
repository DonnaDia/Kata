#Vers 1
def set_alarm(employed, vacation):
    return employed and not vacation


#Vers 2
def set_alarm(employed, vacation):
    return True if employed and not vacation else False