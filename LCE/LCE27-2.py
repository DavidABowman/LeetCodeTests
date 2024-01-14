#Given an integer array nums and an integer val, remove all occurrences of val in nums in-place
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        #Initialise 2 pointers
        i = 0 #'i' is used to iterate through the array
        k = 0 #'k' is used to keep track of no. of elements != val
        
        while i < len(nums): #Iterate through array
            if nums[i] != val: #If current element != val
                nums[i], nums[k] = nums[k], nums[i] #Swap currElement w/ element at index k
                k += 1 #Move both pointers forward
            i += 1 #Move iterator pointer forward
        return k #First k elements now contain elements != val, so ignore rest of elements

'''
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        index = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[index] = nums[i]
                index += 1
        return index

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