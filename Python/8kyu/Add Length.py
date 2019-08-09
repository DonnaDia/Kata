#Vers.1
def add_length(str_):
    return ["%s %d" % (w, len(w)) for w in str_.split()]

#Vers.2
def add_length(str_):
    arr = []
    for element in list(str_.split(' ')):
        arr.append(str(element) + " " + str(len(element)))
    return arr   