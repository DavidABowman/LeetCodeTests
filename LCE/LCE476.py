#Given an integer num, return its complement.
#The complement of an integer is the integer you get 
#when you flip all the 0's to 1's and all the 1's to 0's in its binary representation.

class Solution:
    def findComplement(self, num: int) -> int:
        binary_num = bin(num)[2:]
        complement = ''.join(['1' if bit == '0' else '0' for bit in binary_num])
        complement_int = int(complement, 2)
        return complement_int