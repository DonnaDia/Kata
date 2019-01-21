def binary_to_string(binary):
    return ''.join( chr(int(b, 2)) for b in binary[2:].split('0b') )