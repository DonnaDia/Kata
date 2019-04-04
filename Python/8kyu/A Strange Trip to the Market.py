#Vers1
def say_hello(name, city, state):
	return f"Hello, {','.join(name).replace(',', ' ')}! Welcome to {city}, {state}!"


#Vers2
def say_hello(name, city, state):
	name = ','.join(name).replace(',', ' ')
	return f"Hello, {name}! Welcome to {city}, {state}!"


#Vers3
def say_hello(name, city, state):
    name = " ".join(name)
    return ("Hello, " + name + "! Welcome to " + city + ", " + state + "!") 