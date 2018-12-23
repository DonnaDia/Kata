#Vers 1
def correct_tail(body, tail):
    return True if body[-1] == tail[0] else False

#Vers 2
def correct_tail(body, tail):
    if body[-1] == tail[0]:
        return True
    else:
        return False