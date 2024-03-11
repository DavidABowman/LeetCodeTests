#Write a function that takes the binary representation of an unsigned integer 
#and returns the number of '1' bits it has (also known as the Hamming weight).

class Solution:
    def hammingWeight(self, n: int) -> int:
        #Initialise count to store the number of '1' bits
        count = 0
        #Iterate until n becomes 0
        while n:
            #Increment count if the last bit is 1
            count += n & 1
            #Right shift n to check the next bit
            n >>= 1
        return count
'''
class Solution:
    def hammingWeight(self, n: int) -> int:
        return bin(n)[2:].count('1')        
    #Count total 1 in number
    #Return total value
'''