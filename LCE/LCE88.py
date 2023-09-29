#You are given two integer arrays nums1 and nums2, 
#sorted in non-decreasing order, and two integers m and n,
#representing the number of elements in nums1 and nums2 respectively.

#Merge nums1 and nums2 into a single array sorted in non-decreasing order.

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

'''        
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