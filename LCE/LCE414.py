#Given an integer array nums, return the third distinct maximum number in this array. 
#If the third maximum does not exist, return the maximum number

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        n, T = list(set(nums)), [float('-inf')]*3
        for i in n:
            if i>T[0]:
                T = [i,T[0],T[1]]
                continue
            if i>T[1]:
                T = [T[0], i, T[1]]
                continue
            if i>T[2]:
                T = [T[0], T[1], i]
        return T[2] if T[2] != float('-inf') else T[0]