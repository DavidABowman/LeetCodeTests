#Given a string s, find the first non-repeating character in it and return its index. 
#If it does not exist, return -1.

class Solution:
    def firstUniqChar(self, s: str) -> int:
        hset = collections.Counter(s)
        #Traversing the string from the beginning
        for idx in range(len(s)):
            if hset[s[idx]] == 1:
                return idx #If count = 1, its frirst distinct chr in list
        return -1