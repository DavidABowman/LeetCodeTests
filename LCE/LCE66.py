#You are given a large integer represented as an integer array digits,
# where each digits[i] is the ith digit of the integer

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        strings = " "
        for number in digits:
            strings += str(number)

        temp = str(int(strings) +1)

        return [int(temp[i]) for i in range(len(temp))]     
        