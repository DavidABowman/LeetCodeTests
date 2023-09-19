#Remove Duplicates from Sorted Array

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        j = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[j] = nums[i]
                j += 1
        return j


'''
#Create Temporary Auxilliary Array to store Unique Elements, copying one by one from Arr to Temp - Keeping count with integer j, and copying j elements to and from temp 
class Solution:
    def removeDuplicates(arr, n):
        if n == 0 or n == 1:
            return n
        temp = list(range(n))

        j = 0
        for i in range(0, n-1):
            if arr[i] != arr[i+1]:
                temp[j] = arr[i]
                j += 1
        temp[j] = arr[n-1]
        j += 1

        for i in range(0, j):
            arr[i] = temp[i]
        return j
'''