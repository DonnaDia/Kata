#Vers 1
def cube_times(times):
    results = (round(sum(sorted(times)[1:-1]) / 3, 2), sorted(times)[0])
    
    return results


#Vers 2
def cube_times(times):
    fastest_time = min(times)
    times.remove(max(times))
    times.remove(min(times))
    results = (round(sum(times) / 3, 2), fastest_time)
    
    return results