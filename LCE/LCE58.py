#Given a string s consisting of words and spaces, 
#return the length of the last word in the string.

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.split()[-1])
    
'''
#This one was fun to learn from, in all honesty. I enjoyed it :)
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        ss = s.strip()
        a = ss.split(" ")
        return len(a[-1])
'''