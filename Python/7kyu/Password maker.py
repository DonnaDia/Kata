def make_password(phrase):
    if 'i' in phrase or 'I' in phrase or 'o' in phrase or 'O' in phrase\
            or 's' in phrase or 'S' in phrase:
        phrase = phrase.replace('i','1')
        phrase = phrase.replace('I','1')
        phrase = phrase.replace('o', '0')
        phrase = phrase.replace('O','0')
        phrase = phrase.replace('s', '5')
        phrase = phrase.replace('S','5')

    phrase = list(phrase.split(' '))

    password = []
    for elem in phrase:
        password.append(elem[0:1])

    password = ','.join(password)
    password = password.replace(',', '')

    return password