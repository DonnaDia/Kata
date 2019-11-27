#Vers 1
def hoop_count(n):
    return "Great, now move on to tricks" if n >= 10 else "Keep at it until you get it"


#Vers 2
def hoop_count(n):
    if n >= 10:
        return "Great, now move on to tricks"
    else:
        return "Keep at it until you get it"