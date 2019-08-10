#Version 1
def reverseWords(str):
    for line in str.split('\n'):
        return(' '.join(line.split()[::-1]))

#Version 2
def reverseWords(str):
    return ' '.join(reversed(str.split(' ')))