#Version 1
hello = lambda name='':f"Hello, {name.title() or 'World'}!"


#Version 2
def hello(name=''):
    return f"Hello, {name.capitalize() if name else 'World'}!"

#Version 3
def hello(name=''):
    if name == '' or name == ' ':
        return 'Hello, World!'
    else:
        name = name.capitalize()
        return f'Hello, {name}!'    