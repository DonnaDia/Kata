def abbrevName(name):
    first_name = name
    last_name = name.split()
    return first_name[0][0].upper() + "." + last_name[1][0].upper()