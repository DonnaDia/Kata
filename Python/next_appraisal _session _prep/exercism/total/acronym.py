def abbreviate(words):
    if '-' in words:
        words = words.replace('-', ' ')

    words = words.upper().split(' ')
    abbreviation = []

    for word in words:
        if '_' in word:
            words[words.index(word)] = word.strip('_')

    abbreviation += [word[0] for word in words if len(word) >= 1]

    return ''.join(abbreviation)