#Given a non-empty array of integers nums, every element appears twice except for one. 
#Find that single one.

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return reduce(lambda total, el: total ^ el, nums)

'''
I'm aware I should use bitwise operators
I know 2 numbers will repeat - so I can just use XOR to cancel them
E.g 15 & 15 = 1111 & 1111
Thus, XOR would lead the remainder to be 0
Therefore, the only answer must be anything that
can't pair with any other number to have a remainder of 0, or r>0 
  nums.reduce(:^) doens't work 
'''