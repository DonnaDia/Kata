#Vers 1
def calculate_total(t1, t2):
    return sum(t1) > sum(t2)



#Vers 2
def calculate_total(t1, t2):
    return True if sum(t1) > sum(t2) else False