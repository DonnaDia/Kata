import re

def validate_code(code):
    return True if re.match("^[1-3]", str(code)) else False