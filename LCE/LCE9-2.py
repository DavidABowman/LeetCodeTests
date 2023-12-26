#Given an integer x, return true if x is a palindrome, and false otherwise.
#No strings attatched
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        original_x, reversed_x = x, 0
        while x > 0:
            digit = x % 10
            reversed_x = reversed_x * 10 + digit
            x //= 10

        return original_x == reversed_x

'''
2nd attempt
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        x_str = str(x)
        return x_str == x_str[::-1]


1st attempt
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        if str(x) == (str(x)[::-1]):
            return True
'''