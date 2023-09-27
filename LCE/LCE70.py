#You are climbing a staircase. It takes n steps to reach the top.
#Each time you can either climb 1 or 2 steps. 
#In how many distinct ways can you climb to the top?

class Solution:
    def climbStairs(self, n: int) -> int:
        a, b = 0, 1
        for i in range(n):
            a, b = b, a + b
        return b
    

#Ultimately, this process turned out to be quite slow (Beats 22%)
#I'm assuming this is due to the for loop adding a bunch of times
#Nevertheless, though I didn't write the code - I can confidently say
#I understand 100% of it. I spent a while writing a bunch of maths notes
#Plus a bunch more that led to nowhere, but I'm happy nevertheless.

