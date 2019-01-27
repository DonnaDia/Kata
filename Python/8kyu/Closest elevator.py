#Vers 1
def elevator(left, right, call):
    return "left" if abs(call - left) < abs(call - right) else "right"

#Worked on my machine - 1
def elevator(left, right, call):
    if call >= right: return 'right'
    if call > left: return 'right'
    if call == right == left: return 'right'
    else: return 'left'


print(elevator(0,1,0))
print(elevator(0,1,1))
print(elevator(0,1,1))
print(elevator(0,0,0))
print(elevator(0,2,1))    

#Worked on my machine - 2
def elevator(left, right, call):
    return 'left' if call == left and left!=right else 'right' if left == right == call else 'right'


print(elevator(0,1,0))
print(elevator(0,1,1))
print(elevator(0,1,1))
print(elevator(0,0,0))
print(elevator(0,2,1))
