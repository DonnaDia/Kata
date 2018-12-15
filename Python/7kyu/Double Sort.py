Double Sort

#Vers1
def db_sort(arr):
    return(sorted(arr, key = lambda char:(isinstance(char,str),char)))

#Vers2
def db_sort(arr):
    nums = []
    words = []
    result = []
    for element in arr:
        if type(element) == int:
            nums.append(element)
        elif type(element) == str:
            words.append(element)
    nums = sorted(nums)
    words = sorted(words)

    result = nums + words
    
    return result