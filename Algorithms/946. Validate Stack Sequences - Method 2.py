# Given two integer arrays pushed and popped each with distinct values, 
# return true if this could have been the result of a sequence of push and pop operations on an initially empty stack, or false otherwise.


class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        
        if pushed == popped or popped == pushed[::-1]:
            return True

        for i in pushed:
            stack.append(i)
            while stack:
                if stack[-1] == popped[0]:
                    stack.pop()
                    del(popped[0])
                else:
                    break
        
        if popped == stack[::-1]:
            return True
        else:
            return False
