
#Remove Element
#Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. 



class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        index = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[index] = nums[i]
                index += 1
        return index
'''
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        for i in nums[:]:
            if i == val:
                nums.remove(i)
        return len(nums)

#class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        count = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[count] = nums[i]
                count += 1
            return count

#class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        j = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[j] = nums[i]
                j += 1
        return j
'''