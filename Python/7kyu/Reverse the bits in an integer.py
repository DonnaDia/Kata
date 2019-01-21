#Vers 1
def reverse_bits(n):
    return int(bin(n)[:1:-1],2)


#Vers 2
def reverse_bits(i):
    return int((bin(i))[2:][::-1],2)


#Vers 3
def reverse_bits(i):
    return int(str(bin(i))[::-1].replace('b','')[:-1],2)