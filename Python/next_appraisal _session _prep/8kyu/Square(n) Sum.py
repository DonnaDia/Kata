#Vers 1
def square_sum(numbers):
    return sum(x ** 2 for x in numbers)

#Vers 2
def square_sum(numbers):
        return sum([num ** 2 for num in numbers])

#Vers 3
def square_sum(numbers):
    return sum(number ** 2 for number in numbers)