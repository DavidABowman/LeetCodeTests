#Given two integer arrays nums1 and nums2, return an array of their intersection. 
#Each element in the result must be unique and you may return the result in any order.

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        d = {}
        res = []
        for n in nums1:
            d[n] = 1

        for n in nums2:
            if n in d and d[n]:
                res.append(n)
                d[n] -= 1
        return res