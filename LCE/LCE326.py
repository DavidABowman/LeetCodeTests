#Given an integer n, return true if it is a power of three. Otherwise, return false.

from math import log
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        
        #:type n: int
        #:rtype: bool

        if n<= 0: return False
        res = round(log(n,3))
        return 3**res == n