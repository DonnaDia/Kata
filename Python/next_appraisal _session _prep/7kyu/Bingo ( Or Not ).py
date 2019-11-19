def bingo(array): 
    verdict = list()
    bingo_indexes = [2, 9, 14, 7, 15]
    
    for num in array:
        if num in bingo_indexes:
            verdict.append(num)
            
    return "WIN" if sum(set(verdict)) ==  47 else "LOSE"  