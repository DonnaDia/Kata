#Vers.1(educational)
def basic_op(operator, value1, value2):
    #your code here
    if operator == "+":
        return value1 + value2
    elif operator == "-":
        return value1 - value2
    elif operator =="*":
        return value1 * value2
    else:
        return value1 / value2

#Vers.2
def basic_op(operator, value1, value2):
    return eval("{}{}{}".format(value1, operator, value2))