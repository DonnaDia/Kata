#Vers2
def types(x):
    return 'int' if type(x) == int else 'float' if type(x) == float\
    else 'str' if type(x) == str else 'bool'

#LongVers
def types(x):
    if type(x) == int:
        print('int')
    elif type(x) == float:
        print('float')
    elif type(x) == str:
        print('str')
    elif type(x) == bool:
        print('bool')

types(21)
types(9.7)
types("Hello")
types(True)