#Vers 1
def filter_numbers(string):
    return "".join(x for x in string if not x.isdigit())


#Vers 2
def filter_numbers(string):
    s = ''
    for el in string:

        try:
            int(el)
        except:
            s += el

    return s