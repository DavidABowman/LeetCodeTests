#Given a positive integer num, return true if num is a perfect square or false otherwise.

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        return int(num**0.5) == num**0.5
'''
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if sqrt(num)%1 == 0:
            return True

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        left, right = 1, num
        while left <= right:
            mid = (left + right) // 2
            if mid * mid == num:
                return True
            elif mid * mid < num:
                left = mid + 1
            else:
                right = mid - 1
        return False
'''