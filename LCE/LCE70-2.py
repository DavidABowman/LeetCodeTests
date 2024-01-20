#You are climbing a staircase. It takes n steps to reach the top.
#Each time you can either climb 1 or 2 steps. 
#In how many distinct ways can you climb to the top?

#2nd Try
class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        
        ways = [0] * (n+1)

        ways[1] = 1
        ways[2] = 2

        for i in range(3, n+1):
            ways[i] = ways[i - 1] + ways[i - 2]
        return ways[n]

'''
class Solution:
    def climbStairs(self, n: int) -> int:
        a, b = 0, 1
        for i in range(n):
            a, b = b, a + b
        return b
'''    