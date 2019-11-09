#Vers 1
def growing_plant(upSpeed, downSpeed, desiredHeight):
    days = 1
    daily_growth = upSpeed - downSpeed
    height = upSpeed
    
    while height < desiredHeight:
        height += daily_growth
        days += 1
        

#Vers 2
def growing_plant(upSpeed, downSpeed, desiredHeight):
    days_to_wait = 0
    daily_speed = upSpeed - downSpeed
    start = 0 
    
    if upSpeed >= desiredHeight:
        days_to_wait = 1
    else:  
        while start < desiredHeight:
            start += daily_speed
            days_to_wait += 1
            if start + upSpeed >= desiredHeight:
                days_to_wait += 1
                break
                
    return days_to_wait