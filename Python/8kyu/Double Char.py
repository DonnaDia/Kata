#Version 1
def double_char(s):
    return ''.join(letter * 2 for letter in s)

#Version 2
def double_char(s):
    return ''.join([i+i for i in s])