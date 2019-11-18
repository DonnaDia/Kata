#Vers 1
def nb_year(population, percent, newcomers, target):
    years = 0 
    
    while population < target:
        population += population * (percent * 0.01) + newcomers
        years += 1
        
    return years    


#Vers 2
def nb_year(p0, percent, aug, p):
    years = 0
    percent = percent * 0.01

    while p0 < p:
        p0 += int(p0  * percent + aug)
        years += 1
        
    return years    