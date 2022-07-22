# You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. 
# The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.

# Increment the large integer by one and return the resulting array of digits.


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num_digit = len(digits) - 1
        num = 0
        for i in digits:
            num += 10**num_digit * i
            num_digit -= 1
        return [int(i) for i in str(num+1)]
