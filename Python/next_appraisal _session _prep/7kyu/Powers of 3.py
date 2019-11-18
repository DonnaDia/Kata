def largestPower(N):
    result = 0
    
    while (3 ** result < N):
        result += 1
    
    return result - 1