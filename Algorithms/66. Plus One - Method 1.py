# You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. 
# The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.

# Increment the large integer by one and return the resulting array of digits.


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if digits[-1] != 9:
            digits[-1] += 1
            return digits
        digits[-1] = 0
        rest_digit = len(digits) - 2
        while rest_digit >= 0:
            if digits[rest_digit] != 9:
                digits[rest_digit] += 1
                return digits
            else:
                digits[rest_digit] = 0
                rest_digit -= 1
        digits.insert(0, 1)
        return digits
