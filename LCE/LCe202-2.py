#A happy number is a number defined by the following process:

#Starting with any positive integer, replace the number by the sum of the squares of its digits.
#Repeat the process until the number equals 1 (where it will stay), 
#or it loops endlessly in a cycle which does not include 1.
#Those numbers for which this process ends in 1 are happy.

#W will return to this 
#Iterative
class Solution:
    def isHappy(self, n: int) -> bool:
        visted = set()

        while n != 1 and n not in visted:
            visted.add(n)
            n = sum(int(digit) ** 2 for digit in str(n))
        return n == 1
'''
#Recursive
class Solution:
    def isHappy(self, n: int) -> bool:
        return  False if  n in [2,3,4,5,6,8,9] else True if n == 1 else self.isHappy(sum(pow(int(digit),2) for digit in str(n)))
        '''