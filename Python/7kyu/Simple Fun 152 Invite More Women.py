#Vers 1
def invite_more_women(arr):
    return True if sum(arr) > 0 else False

#Vers 2
def invite_more_women(arr):
    return True if arr.count(1) > arr.count(-1) else False

#Vers 3
def invite_more_women(arr):
    men = len([i for i in arr if i > 0])
    women = len([i for i in arr if i < 0])
    
    return True if men > women else False