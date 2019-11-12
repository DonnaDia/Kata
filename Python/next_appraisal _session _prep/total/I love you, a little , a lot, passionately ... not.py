#Vers 1
def how_much_i_love_you(nb_petals):
    phrases = {1: 'I love you', 2: 'a little', 3: 'a lot', 
               4: 'passionately', 5: 'madly', 6: 'not at all'}
                   
    if nb_petals > 6:
        petal = nb_petals % 6 if nb_petals % 6 != 0 else 6

    else:
        petal = nb_petals
        
    return phrases[petal]     
        

#Vers 2
def how_much_i_love_you(nb_petals):
    phrases = {1: 'I love you', 2: 'a little', 3: 'a lot', 
               4: 'passionately', 5: 'madly', 6: 'not at all'}
               
    petal = 0
    
    if nb_petals > 6:
        petal = nb_petals % 6 if nb_petals % 6 != 0 else 6

    else:
        petal = nb_petals
        
    return phrases[petal] 