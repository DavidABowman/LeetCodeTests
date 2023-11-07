#Given an integer n, return true if n is an ugly number
'''
class Solution:
    def isUgly(self, n: int) -> bool:
        if n == 0:
            return False
        res=[2, 3, 5]
        while n!= 1:
            for i in res:
               if n%i==0:
                   n=n//i
                   break
            else:
                return False
        return True
'''

#Dry Run
class Solution:
    def isUgly(self, n: int) -> bool:
        if n == 0:
            return False
        while n != 1:
            if n % 2 == 0:
                n /= 2
            elif n % 3 == 0:
                n /= 3
            elif n % 5 == 0:
                n /= 5
            else:
                return False
        return True
'''
class Solution:
    def isUgly(self, n: int) -> bool:
        if n == 0:
            return 0
        for i in 2, 3, 5:
            while n%1 == 0:
                n//i
        return n == 1
'''