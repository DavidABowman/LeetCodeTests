#Given a string s, return true if it is a palindrome, or false otherwise.

class Solution:
    def isPalindrome(self, s: str) -> bool:
        #Convert the string to lowercase and remove non-aplhanumerical characters
        cleaned_s = ''.join(char.lower() for char in s if char.isalnum())
        #Check if cleanmed string equal to reverse
        return cleaned_s == cleaned_s[::-1] 
'''
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s1 = ''
        for c in s.lower():
            if c.isalnum():
                s1 += c

        return True if s1==s1[::-1] else False

class Solution:
    def isPalindrome(self, s: str.isalnum) -> bool:
        if s == (s[::-1]):
            return True
        else:
            return False
            '''
