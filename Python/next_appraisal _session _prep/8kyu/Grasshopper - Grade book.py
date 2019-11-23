#Vers 1
def get_grade(s1, s2, s3):
    return {6:'D', 7:'C', 8:'B', 9:'A', 10:'A'}.get((s1 + s2 + s3) // 30, 'F')


#Vers 2
def get_grade(s1, s2, s3):
    total = sum([s1 + s2 + s3]) // 3
    
    if total >= 90: return 'A'
    if total >= 80: return 'B'
    if total >= 70: return 'C'
    if total >= 60: return 'D'
    return 'F'
    

#Vers 3
def get_grade(s1, s2, s3):
    total = (s1 + s2 + s3) // 3
    
    if total in range(90, 101):
        return 'A'
    elif total in range(80, 90):
        return 'B'
    elif total in range(70, 80):
        return 'C'
    elif total in  range(60, 70):
        return 'D'
    else:
        return 'F'