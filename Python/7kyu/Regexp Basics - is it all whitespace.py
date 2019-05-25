import re

def whitespace(string):
    return True if re.match('^\s*$', string) else False