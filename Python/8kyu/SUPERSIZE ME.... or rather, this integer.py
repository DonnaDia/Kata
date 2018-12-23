def super_size(n):
    n_list = sorted(list(str(n)))
    n_list.reverse()
    return int("".join(tuple(n_list)))