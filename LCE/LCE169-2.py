#Given an array nums of size n, return the majority element.

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        #Initialise the candidate and its count
        candidate = nums[0]
        count = 1
        #Iterate through the array
        for num in nums [1:]:
            #If count becomes 0, update the candidate
            if count == 0:
                candidate = num
                count = 1
            #If the current number is the same as the candidate, increment count
            elif num == candidate:
                count += 1
            #If the candidate number is different from the candidate, decrement count
            else:
                count -= 1
            return candidate
'''
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        candidates = None
        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1)
        return candidate

#Boyer–Moore majority vote algorithm
#Initialize an element m and a counter i with i = 0
#For each element x of the input sequence:
#If i = 0, then assign m = x and i = 1
#else if m = x, then assign i = i + 1
#else assign i = i − 1
#Return m
'''