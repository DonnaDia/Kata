#Vers 1
def shorten_to_date(long_date):
    return long_date.split(',')[0]


#Vers 2
def shorten_to_date(long_date):
    date = long_date.split(' ')[:-1]
    date = ','.join(date).replace(',', ' ')[:-1]
    return date