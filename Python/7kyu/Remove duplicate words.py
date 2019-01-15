#Vers 1
def remove_duplicate_words(x):
    x = x.split()

    words = []
    for word in x:
        if word not in words:
          words.append(word)

    return ' '.join(words)


#Vers 2
def remove_duplicate_words(x):
    x = x.split()

    words = []
    for word in x:
        if word not in words:
            words.append(word)

    words = ' '.join(words)
    
    return words