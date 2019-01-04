#Vers 1
def calculate(x):
    return str(eval(x.replace('plus', '+').replace('minus', '-')))

#Vers 2
def calculate(x):
    if 'plus' or 'minus' in x:
        x = x.replace('plus', '+').replace('minus', '-')
    return str(eval(x))