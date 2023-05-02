# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def recursive(left, right, cur):
            if left <= right:
                if left == 0 and right == 0:
                    output.append(cur)
                    return
                if left > 0:
                    recursive(left-1, right, cur+'(')
                if right > 0:
                    recursive(left, right-1, cur+')')
        
        output = []
        recursive(n, n, '')
        return output
