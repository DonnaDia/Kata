#Vers 1. easy and dull
def alias_gen(f_name, l_name):
        name = FIRST_NAME.get(f_name[0].upper())
        surname = SURNAME.get(l_name[0].upper())
        return "{} {}".format(name, surname) if name and surname else \
        "Your name must start with a letter from A - Z."

#Vers 2. a bit comlicated and with regex
def alias_gen(f_name, l_name):
    pattern = '[A-Za-z]'
    if re.match(pattern, f_name) and re.match(pattern, l_name):
        name_key = f_name[0].upper()
        surname_key = l_name[0].upper()
        gen = "{} {}".format(FIRST_NAME[name_key], SURNAME[surname_key])
        return gen
    else:
        return "Your name must start with a letter from A - Z."