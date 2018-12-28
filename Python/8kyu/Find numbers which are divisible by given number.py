#Vers 1
def divisible_by(numbers, divisor):
    return [element for element in numbers if element % divisor == 0]

#Vers 2
def divisible_by(numbers, divisor):
    result = []
    for element in numbers:
        if element % divisor == 0:
            result.append(element)
            
    
    return result