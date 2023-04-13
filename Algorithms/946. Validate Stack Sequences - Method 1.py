# Given two integer arrays pushed and popped each with distinct values, 
# return true if this could have been the result of a sequence of push and pop operations on an initially empty stack, or false otherwise.


class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        index_push = 0
        index_pop = 0

        while index_push < len(pushed) and index_pop < len(popped):
            if pushed[index_push] == popped[index_pop]:
                pushed.pop(index_push)
                index_pop += 1
                if index_push != 0:
                    index_push -= 1
            else:
                index_push += 1
        
        index_push -= 1
        
        while index_pop < len(popped):
            if pushed[index_push] == popped[index_pop]:
                pushed.pop(index_push)
                index_pop += 1
                index_push -= 1
            else:
                return False
        
        return True
