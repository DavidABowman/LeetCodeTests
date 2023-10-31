#Given an integer n, return true if it is a power of two. Otherwise, return false.

#An integer n is a power of two, if there exists an integer x such that n == 2x.

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return bin(n)[2] == "1" and bin(n).count("1") == 1

        #Ong this was a nice easy question
        #Powers of 2 will only be represented by 1 bit, so we count the amount of bits
        #the number takes, if 1 then true