#Reverse bits of a given 32 bits unsigned integer.

class Solution:
    def reverseBits(self,n: int) -> int:
        r = 0
        count = 32
        while count:
            r <<= 1 #Shift r to the left to make room for the next bit
            r |= n & 1 #Set the least sig. bit of r to the current bit of n
            n >>= 1 #Shift n to the right to get to the next bit
            count -= 1 #Decrement count to keep track of the remaining bits
        return r
'''
class Solution:
    def f(self,n,r,count):
        if n<1:
            return r<<(32-count)
        return self.f(n>>1,(r<<1)|(n&1),count+1)
    def reverseBits(self, n: int) -> int:
        return self.f(n,0,0)
#Don't understand yet, but I'll understand it soon

class Solution:
    def reverseBits(self, n: int) -> int:
        int(n[::-1])
        return n

Want to reverse code
  int::-1
Want to convert from 32bit to denary
00000100
(0 x 2^7)+(0x 2^7)+...+(1 x 2^2)+...+(0x 2^0)
Have to do it in this order - I think - otherwise, we are converitng binary to denary and 
reversing denary, not reversing binary and outputting denary

'''