#Vers 1
def Descending_Order(num):
    return int("".join(sorted(str(num), reverse=True)))


#Vers 2
def Descending_Order(num):
    num = list(str(num))
    desc = int("".join(sorted(num, reverse=True)))
    
    return desc


#Vers 3
def Descending_Order(num):
    num = int(''.join(sorted(str(num), reverse=True)))

    return num


#Vers 4
def Descending_Order(num):
    num = str(num)
    num = ''.join(sorted(num))
    num = sorted(num, reverse=True)
    num = ','.join(num)
    num = int(num.replace(',', ''))
    return num