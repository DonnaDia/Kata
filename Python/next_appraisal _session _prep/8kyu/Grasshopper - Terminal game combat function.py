#Vers 1
def combat(health, damage):
    return max(health - damage, 0)

#Vers 2
def combat(health, damage):
    result = health - damage
    
    return result if result > 0 else 0