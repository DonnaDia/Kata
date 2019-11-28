#Vers 1
def is_vow(inp):
    return [chr(char) if chr(char) in 'aeiou' else char for char in inp]


#Vers 2
def is_vow(inp):
    vowels = ['a', 'e', 'i', 'o', 'u']
    verification = [chr(char) if chr(char) in vowels else char for char in inp]
    
    return verification