# Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

# Implement the MinStack class:

# MinStack() initializes the stack object.
# void push(int val) pushes the element val onto the stack.
# void pop() removes the element on the top of the stack.
# int top() gets the top element of the stack.
# int getMin() retrieves the minimum element in the stack.
# You must implement a solution with O(1) time complexity for each function.


class MinStack:
    def __init__(self):
        self.stack = []
        self.min = float('inf')
        
    def push(self, val: int) -> None:
        self.stack.append((val, self.min))
        self.min = min(self.min, val)

    def pop(self) -> None:
        self.min = self.stack[-1][1]
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.min
