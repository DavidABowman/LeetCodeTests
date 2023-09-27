#Given a non-negative integer x,
#return the square root of x rounded down to the nearest integer

class Solution: # Binary Search Method
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        first, last = 1, x
        while first <= last:
            mid = first + (last - first) // 2
            if mid == x // mid:
                return mid
            elif mid > x // mid:
                last = mid - 1
            else:
                first = mid + 1
        return last


'''
Thought Process
Have to think of different ways to visualise SqRt IMO
Obviosuly you have the function ^ 1/2
    What does this mean - how can we comprehend it though? (Not too important though)
Number Divided by Itself? - NO (Would be 1), number multiplied by 1/n (Also no as it = 1)
n^3 = n*n*n
n^2 = n*n
n^1/2 = 1/(n*n)? NO, that's n^-2 = 1/n^2 = 1/(n*n)

'''

'''
#First Proper LeetCode Thing I Get Write With No Outside Help
#Defies Rules of the Problem Though haha
class Solution:
    def mySqrt(self, x: int) -> int:
        return int(x**0.5)
'''