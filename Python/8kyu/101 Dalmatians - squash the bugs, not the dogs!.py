#Vers1
def how_many_dalmatians(n):
    dogs = ["Hardly any", "More than a handful!", "Woah that's a lot of dogs!", "101 DALMATIONS!!!"]
    return dogs[0] if n <= 10 else dogs[1] if n <=50 else dogs[3] if n == 101 else dogs[2]

#Vers2    
def how_many_dalmatians(n):
    dogs = ["Hardly any", "More than a handful!", "Woah that's a lot of dogs!", "101 DALMATIONS!!!"];
    number = n

    if number <= 10:
        respond = dogs[0]
    elif number <= 50:   
        respond = dogs[1]
    elif number == 101:
        respond = dogs[3]
    else:
        respond = dogs[2]  

    return respond