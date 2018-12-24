#Works-on-my-machine Vers
def odd_count(n):
    nums = []
    for number in range(0, n):
        if number % 2 != 0:
            nums.append(number)

    return len(nums)

print(odd_count(15023))


#Vers2
def odd_count(n):
    nums = []
    for number in range(1, n, 2):
         nums.append(number)

    return len(nums)

print(odd_count(15023))

#Vers3
def odd_count(n):
    return n // 2