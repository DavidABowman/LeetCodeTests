#Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
#You may assume that each input would have exactly one solution, and you may not use the same element twice.
#You can return the answer in any order

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hashmap:
                return [i, hashmap[complement]]
            hashmap[nums[i]] = i
''' 
Original Attempt - 45mins


def add(x,y):
    return x+y
print(add(4,5))

print((lambda x,y: (x+y))(1,9))

def map(func, iter):
    result = [] #EmptyList
    for item in iter:
        new_item = func(item)
        result.append(new_item)
    return(result)
nums = [2, 7, 11, 15]
cube = map(lambda x: x**3, nums)
print(cube)
'''