#The Hamming distance between two integers is the number of positions 
#at which the corresponding bits are different.

'''
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        xor_result = x ^ y
        hamming_distance = 0
        while xor_result:
            hamming_distance += xor_result & 1
            xor_result >>= 1
        return hamming_distance
'''

class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        return bin(x^y).count('1')