#Vers 1
def name_shuffler(str_):
    return ' '.join(str_.split(' ')[::-1])


#Vers 2
def name_shuffler(str_):
    str_ = str_.split(' ')
    result = str(str_[1] + ' ' + str_[0])
    return result