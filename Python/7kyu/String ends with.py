#Vers 1
def solution(string, ending):
    return string.endswith(ending)


#Vers 2
def solution(a,b):
    return True if b == a[-1:] or b == a[-2:] or b == a[-3:] or b == a[-4:] else False