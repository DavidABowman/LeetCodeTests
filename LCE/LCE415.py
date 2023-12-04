#Given two non-negative integers, num1 and num2 represented as string, 
#return the sum of num1 and num2 as a string.

class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        def strToInt(num):
            result = 0
            for n in num:
                result = result * 10 + ord(n) - ord('0')
            return result
        return str(strToInt(num1) + strToInt(num2))