#Given an integer n, return true if it is a power of four. Otherwise, return false.
        
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        return n>0 and log(n,4).is_integer()
'''
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        return not n & (n - 1) and n.bit_length() % 2

class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        return (n & n - 1) == 0 and (n - 1) % 3 == 0

class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        return bin(n)[4] == "1" and bin(n).count("1") == 1
    #Doesnt Work  :(

class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n<= 0: return False
        res = round(log(n,4))
        return 4**res == n
'''