#You are given two integer arrays nums1 and nums2, 
#sorted in non-decreasing order, and two integers m and n, 
#representing the number of elements in nums1 and nums2 respectively.
#Merge nums1 and nums2 into a single array sorted in non-decreasing order

#Try 2
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        #Initialise Pointers for num1 and num2
        i, j, k = m - 1, n - 1, m + n -1
        #Merge nums1 and 2 from end
        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1
        #If there are remaining elements in nums2, copy them to nums1
        while j >= 0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1

'''
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        idx = 0
        for i in range(len(nums1)):
            if idx >= n:
                break
            if nums1[i] == 0:
                nums1[i]=nums2[idx]
                idx += 1
        nums1.sort()
     
        cur = dummy = ListNode()
        while nums1 and nums2:               
            if nums1.val < nums2.val:
                cur.next = nums1
                nums1, cur = nums1.next, nums1
            else:
                cur.next = nums2
                nums2, cur = nums2.next, nums2
                
        if nums1 or nums2:
            cur.next = nums1 if nums1 else nums2
            
        return dummy.next
'''