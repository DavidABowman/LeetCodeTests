#Return an array ans of length nums1.length such that ans[i] is the next greater element as described above

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        next_greater = {}
        stack = []

        for num in nums2:
            while stack and num > stack[-1]:
                next_greater[stack.pop()] = num
            stack.append(num)

        for num in stack:
            next_greater[num] = -1

        ans = [next_greater[num] for num in nums1]

        return ans