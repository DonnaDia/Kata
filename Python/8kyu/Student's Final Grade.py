#Vers 1
def final_grade(exam, projects):
    if exam > 90 or  projects > 10: return 100
    if exam > 75 and projects >= 5: return 90
    if exam > 50 and projects >= 2: return 75
    return 0


#Vers 2
def final_grade(exam, projects):
    return 100 if exam > 90 or  projects > 10 else 90 if exam > 75 and projects >= 5\
    else 75 if exam > 50 and projects >= 2 else 0