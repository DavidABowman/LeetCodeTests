#Given an integer array nums, 
#return true if any value appears at least twice in the array, 
#and return false if every element is distinct.

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = {}
        for n in nums:
            if n in seen and seen[n] >= 1:
                return True
            seen[n] = seen.get(n, 0) + 1
        return False