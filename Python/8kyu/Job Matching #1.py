#Vers 1
def match(candidate, job):
    return candidate['min_salary'] * 0.9 <= job['max_salary']

#Vers 2 
def match(candidate, job):
    for (j,c)  in zip(job.values(), candidate.values()):
        return True if j >= c * 0.9 else False