#Version 1
def invert(lst):
    return [n * -1 for n in lst]

#Version 2(educational)
def invert(lst):
    inverted_numbers_list = []
    for number in lst:
        inverted_numbers_list.append(number * -1)
    return inverted_numbers_list

#Version 3(even more educational)
def invert(lst):
    inverted_numbers_list = []
    for number in lst:
        if number > 0:
            inverted_numbers_list.append(number * -1)
        else:
            inverted_numbers_list.append(number * -1)
    return inverted_numbers_list