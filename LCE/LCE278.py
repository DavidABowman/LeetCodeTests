#Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, 
#which causes all the following ones to be bad.
#You are given an API bool isBadVersion(version) which returns whether version is bad. 
#Implement a function to find the first bad version. 

# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        i = 1
        j = n
        while i < j:
            pivot = (i+j) // 2
            if (isBadVersion(pivot)):
                j = pivot
            else:
                i = pivot + 1
        return i