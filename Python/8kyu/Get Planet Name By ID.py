#Vers 1
def get_planet_name(id):
    return "Mercury" if id == 1 else "Venus" if id == 2 else 'Earth' if id == 3 \
    else 'Mars' if id == 4 else 'Jupiter' if id == 5 else 'Saturn' if id == 6 \
    else 'Uranus' if id == 7 else 'Neptune' 

#Vers 2
def get_planet_name(id):
    if id == 1:
        return "Mercury"
    elif id == 2:
        return "Venus"
    elif id == 3:
        return "Earth"
    elif id == 4: 
        return "Mars"
    elif id == 5:
        return "Jupiter"
    elif id == 6:
        return "Saturn"
    elif id == 7:
        return "Uranus"
    elif id == 8:
        return "Neptune"