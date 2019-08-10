#Version 1
def super_size(n):
    return int(''.join(sorted(str(n), reverse = True)))

#Version 2
def super_size(n):
    n_list = sorted(list(str(n)))
    n_list.reverse()
    return int("".join(tuple(n_list)))