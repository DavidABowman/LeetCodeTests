#Given a string s consisting of words and spaces, 
#return the length of the last word in the string.

#Try 2
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        words = s.split()
        if not words:
            return 0
        return len(words[-1])
'''
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.split()[-1])

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        ss = s.strip()
        a = ss.split(" ")
        return len(a[-1])
        '''