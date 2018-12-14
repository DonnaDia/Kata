#Vers1
def count_sheeps(arrayOfSheeps):
  return arrayOfSheeps.count(True)

#Vers2
def count_sheeps(arrayOfSheeps):
    result = 0
    for sheep in arrayOfSheeps:
        if sheep == True:
            result += 1
    return result
