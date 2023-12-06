#Given an array nums of n integers where nums[i] is in the range [1, n], 
#return an array of all the integers in the range [1, n] that do not appear in nums.
'''
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
	      return set(range(1, len(nums) + 1)) - set(nums)

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for n in nums:
            a = abs(n) - 1
            if nums[a] > 0: nums[a] *= -1
        return [i+1 for i in range(len(nums)) if nums[i] > 0]
'''
#My Solution :DD
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for n in nums:
            index = abs(n) - 1
            nums[index] = -abs(nums[index])

        result = [i + 1 for i, n in enumerate(nums) if n > 0]

        return result
