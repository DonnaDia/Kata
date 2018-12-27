#Vers 1
def shortcut( s ):
    for vowel in "aeiou":
        s = s.replace(vowel, "")
    return s


#Vers 2
def shortcut( s ):
    return s.replace('a','').replace('u','').replace('e','').replace('i','').replace('o','')