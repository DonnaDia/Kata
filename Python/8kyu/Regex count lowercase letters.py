#Vers 1
import re
def lowercase_count(string):
    return len(re.findall('[a-z]',string))
just nowRefactor
import re


#Vers 2
def lowercase_count(strng):
    lowers = []
    for char in strng:
        if re.match('[a-z]', char):
            lowers.append(char)
    return len(lowers) 