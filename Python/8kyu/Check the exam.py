#Vers 1
def check_exam(arr1, arr2, result = 0):
    for num1, num2 in zip(arr1, arr2):
        if num1 == num2:
            result += 4
        elif num1 == '' or num2 == '':
            result += 0
        else:
            result -= 1

    return result if result > 0 else 0  


#Vers 2
def check_exam(arr1,arr2):
    result = 0
    for num1,num2 in zip(arr1,arr2):
        if num1 == num2:
            result += 4
        elif num1 == '' or num2 == '':
            result += 0
        else:
            result -= 1   
            
    return result if result > 0 else 0       
  