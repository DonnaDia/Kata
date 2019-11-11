#Vers 1
string_clean = lambda s: "".join(char for char in s if not char.isdigit())

#Vers 2
string_clean = lambda s: __import__('re').sub('\d', '', s)

#Vers 3
import re

def string_clean(s):
    s = re.sub("\d", '', s)

    return s

#Vers 4
def string_clean(s):
    s = "".join([char for char in s if not char.isdigit()])
    
    return s

#Vers 5
def string_clean(s):
    for char in s:
        if char.isdigit():
            s = s.replace(char, '')
            
    return s