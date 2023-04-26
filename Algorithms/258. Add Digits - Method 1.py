# Given an integer num, repeatedly add all its digits until the result has only one digit, and return it.


class Solution:
    def addDigits(self, num: int) -> int:
        num = str(num)

        while len(num) > 1:
            temp = 0
            for i in num:
                temp += int(i)
            num = str(temp)

        return int(num)
