def first_non_consecutive(arr):
    consecutive = [i for i in range(arr[0], arr[-1])]
    for i,x in zip(consecutive, arr):
        if i != x:
            return x
            break