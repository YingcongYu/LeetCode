# Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

# A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        dic = {'2':'abc', '3':'def', '4':'ghi', '5':'jkl', '6':'mno', '7':'pqrs', '8':'tuv', '9':'wxyz'}
        output = []
        length = len(digits)
    
        def recursive(digits, index, dic, output, combination):
            if index == length:
                output.append(combination)
                return
            for i in dic[digits[index]]:
                recursive(digits, index + 1, dic, output, combination + i)

        recursive(digits, 0, dic, output, '')
        return output
