#Vers 1
def bmi(weight, height):
    bmi = weight / (height ** 2)
    if bmi <= 18.5: return "Underweight"
    elif bmi <= 25.0: return "Normal"
    elif bmi <= 30.0: return "Overweight"
    else: return "Obese" 

#Vers 2
def bmi(weight, height):
    index = weight / height ** 2
    if index > 30:
        return 'Obese'
    elif index <= 18.5: 
        return 'Underweight'
    elif index <= 25:
        return 'Normal'
    else:
        return 'Overweight' 