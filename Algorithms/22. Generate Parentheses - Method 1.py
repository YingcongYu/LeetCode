# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def recursive(n, cur):
            if n == 0:
                if cur not in output:
                    output.append(cur)
                return
            for i in range(len(cur)):
                recursive(n-1, cur[:i]+'()'+cur[i:])
        
        output = []
        recursive(n-1, '()')
        return output
