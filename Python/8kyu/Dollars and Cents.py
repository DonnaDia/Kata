#Vers 1
def format_money(amount):
    return f'${amount:.2f}'

#Vers 2
def format_money(amount):
    amount = float(amount)
    return '${0}'.format(format(amount, '.2f'))

#Vers 3
def format_money(amount):
    return '${0}'.format(format(float(amount), '.2f'))