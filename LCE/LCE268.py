#Given an array nums containing n distinct numbers in the range [0, n], 
#return the only number in the range that is missing from the array.

#Gauss
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        return (len(nums) * (len(nums) + 1))//2 - sum(nums)
'''
#Bit Manipulation
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        return reduce(lambda x,y: x ^ y, list(range(len(nums)+1)) + nums) 

HASHING :
- In this Method, We can iterate over all the element upto the n and compare it with the present element by creating the hash map of (n+1).
Time Complexity = O(n)
Space complexity =O(n)
Issue :- Though it is taking the space complexity of N, So we move on to the next Method.

Sum Formula :
- In this we us e the sum formula i.e;
Sn = (N+1)/2 & Sum of all the array(Sa[]).
And after this we subtract the (Sn-Sa[]) to find the Missing Number.
Time Complexity = O(n)
Space complexity =O(1)
Issue :- It can cause the Overflow issue because in this we are adding the element, So if the array element is very large then it can cause Integer Overflow.
To handle out this Overflow we can use the Next Method which is XOR Bit Manipulation.

XOR Bit Manipulation :
- In this we take the XOR of given array and the first n natural number.
Time Complexity = O(n)
Space complexity =O(1)
No Overflow.
'''