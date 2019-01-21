#Vers 1
def calc_type(a, b, res):
    if res == a + b: return "addition"
    if res == a * b: return "multiplication"
    if res == a - b: return "subtraction"
    if res == a / b: return "division"


#Vers 2
def calc_type(a, b, res):
    return "addition" if a + b == res else "subtraction" if a - b == res else "multiplication" if a * b == res else "division"


#Vers 3
def calc_type(a, b, res):
    if res == a + b:
        return 'addition'
    elif res == a - b:
        return 'subtraction'
    elif res == a * b:
        return 'multiplication'
    else:
        return 'division'