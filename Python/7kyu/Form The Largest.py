#Vers 1
def max_number(num):
    return int(''.join(sorted(str(num), reverse=True)))


#Vers 2
def max_number(num):
    num = str(num)
    outp = sorted(num, reverse=True)
    return int(','.join(outp).replace(',', ''))