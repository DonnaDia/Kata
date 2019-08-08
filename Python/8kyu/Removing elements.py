#Vers.1
def remove_every_other(my_list):
    del my_list[1::2]
    return my_list         

#Vers.2
def remove_every_other(my_list):
    return my_list[::2]