#Find the mean (average) of a list of numbers in an array.
#Version 1:
def find_average(nums):
   return sum(nums) / float(len(nums)) if nums else 0

#Version 2:
def find_average(nums):
    return float(sum(nums)) / len(nums) if len(nums) != 0 else 0

#Version 3
def find_average(nums):
    the_sum = 0
    if len(nums) != 0:
        for num in nums:
    	     the_sum = the_sum + num
        return the_sum / round(len(nums))
    else:
        return 0