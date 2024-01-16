#Given a sorted array of distinct integers and a target value, 
#return the index if the target is found. 
#If not, return the index where it would be if it were inserted in order.

#2nd Try
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
                
        return left
        
'''
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums)-1
        while start <= end:
            mid = (start + end)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                end = mid - 1
            else:
                start = mid + 1
        return end+1

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        return nums.index[target]

      
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)
'''