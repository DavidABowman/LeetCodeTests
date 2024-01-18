#given a large integer represented as an integer array,
#Increment the large integer by one and return the resulting array of digits

#2nd try
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        #Start from Rightmost Digit 
        for i in range(len(digits) -1, -1, -1):
            #Increment Current Digit
            digits[i] += 1
            #Check for carry
            if digits[i] < 10:
                #No carry, we are done
                return digits
            else:
                #Carry, set the current digit to 0 and continue w/ the next digit
                digits[i] = 0
            #Once here, there is a carry in the leftmost digit
            #Insert a new digit at the beginnning w/ value 1
        digits.insert(0, 1)
        return digits
'''
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        strings = " "
        for number in digits:
            strings += str(number)

        temp = str(int(strings) +1)

        return [int(temp[i]) for i in range(len(temp))]
'''
        