import string

def words_to_marks(s):
    letters = dict([(letter, index) for index, letter in enumerate(string.ascii_lowercase, 1)])
    total = 0
    
    for letter in s:
        total += letters[letter]
    
    return total