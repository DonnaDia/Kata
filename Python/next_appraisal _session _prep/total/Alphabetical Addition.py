import string

def add_letters(*letters):
    len_check = [letter for letter in letters]
    
    if len(len_check) == 1:
        return letters[0]
    elif len(len_check) == 0:
        return 'z'

    chars = dict([(letter, index) for index, letter in enumerate(string.ascii_lowercase, 1)])
    indexes = dict([(index, letter) for index, letter in enumerate(string.ascii_lowercase, 1)])

    index = 0

    for char in letters:
        index += chars[char]
        if index > 26:
            index = index - 26

    return indexes[index]