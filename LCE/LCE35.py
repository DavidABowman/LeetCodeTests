#Given a sorted array of distinct integers and a target value, 
#return the index if the target is found. 
#If not, return the index where it would be if it were inserted in order.

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
    
'''
#What the f### >_<
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        return nums.index[target]

      
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)
'''