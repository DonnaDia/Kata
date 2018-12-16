#Vers1
def quotable(name, quote):
    return '{} said: "{}"'.format(name, quote)

#Vers2
def quotable(name, quote):
    return ""'{} said: \"{}\"'.format(name,quote)

#Works-on-my-machine Vers
def quotable(name, quote):
    print(f'\'{name} said: "{quote}"\'')

quotable('Grae', 'Practice makes perfect')