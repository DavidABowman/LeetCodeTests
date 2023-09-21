#Find the Index of the First Occurrence in a String

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)
    
#Not being salty, I did know there was a really simple 1 line code
#Since I saw it on a freecodecamp video, but I couldn't find it 
'''
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        location = 0 
        for i in range(len(haystack)):
            if location[i] in needle:
                location += 1
            else:
                return -1
'''
