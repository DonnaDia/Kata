#Vers 1
import re

def validate_usr(username):
    return bool(re.match('[a-z0-9_]{4,16}$', username))



#Vers 2
import re

def validate_usr(username):
    if " " in username:
        return False
    elif len(username) in range(4, 17) and re.match("[a-z_0-9]*$", username):
        return True
    else:
        return False 