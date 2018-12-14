#Version 1
def is_uppercase(inp):
    return inp == inp.upper()

#Version 2
def is_uppercase(inp):
    return inp.isupper()

#Version 3
def is_uppercase(inp):
    if inp == inp.upper():
        return True
    else:
        return False

#Version 4
def is_uppercase(inp):
    return True if inp == inp.upper() else False        