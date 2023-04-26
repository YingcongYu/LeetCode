# Given an integer num, repeatedly add all its digits until the result has only one digit, and return it.


class Solution:
    def addDigits(self, num: int) -> bool:
        while num > 9:
            temp = 0
            while num:
                temp += num % 10
                num = num // 10
                
            num = temp

        return num
