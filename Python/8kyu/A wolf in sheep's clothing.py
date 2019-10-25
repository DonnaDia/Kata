#Vers.1 
def warn_the_sheep(queue):
    sheep = queue[::-1].index('wolf')
    warning = f'Oi! Sheep number {sheep}! You are about to be eaten by a wolf!'
    demand = 'Pls go away and stop eating my sheep'

    return warning if sheep else demand
    
#Vers.2
def warn_the_sheep(queue):
    queue = queue[::-1]
    sheep = queue.index('wolf')

    if queue.index('wolf') == 0:
        return 'Pls go away and stop eating my sheep'
    else:
        return f'Oi! Sheep number {sheep}! You are about to be eaten by a wolf!'
    
#Vers.3
def warn_the_sheep(queue):
    queue = queue[::-1]
    if queue.index('wolf') == 0:
        return 'Pls go away and stop eating my sheep'
    else:
        return 'Oi! Sheep number {}! You are about to be eaten by a wolf!'.format(queue.index('wolf'))