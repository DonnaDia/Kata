#Vers 1
def is_lock_ness_monster(string):
    return any(x for x in ['tree fiddy', 'three fifty', '3.50'] if x in string)


#Vers 2
def is_lock_ness_monster(string):
    return True if 'tree fiddy' in string or '3.50' in string or 'three fifty' in string else False