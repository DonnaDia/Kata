#Vers 1
def case_sensitive(s):
    uppers = [letter for letter in s if letter.isupper()]
    return [not uppers, uppers]


#Works-on-my-machine vers
def case_sensitive(s):
    result = []
    bigs = []
    if s == '':
        result = [True]
        result.append(bigs)
    else:
        for letter in s:
            if letter.isupper():
                bigs.append(letter)
                result = [False]
                result.append(bigs)

            elif letter.islower():
                result = [True]
                result.append(bigs)

    return result