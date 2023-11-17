#Write a function that reverses a string. The input string is given as an array of characters s.
#You must do this by modifying the input array in-place with O(1) extra memory

class Solution:
    def reverseString(self, s: List[str]) -> None:
        #My Way
        s[:] = s[::-1]

"""
class Solution:
    def reverseString(self, s: List[str]) -> None:
        while i<j:
            s[i],s[j] = s[j],s[i]
            i+=1
            j-=1
        return s

class Solution:
    def reverseString(self, s: List[str]) -> None:
        s{::-1} = s
        
class Solution:
    def reverseString(self, s: List[str]) -> None:
        s.reverse()

        Do not return anything, modify s in-place instead.
"""
        