# You are given two non-empty linked lists representing two non-negative integers. 
# The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1 = 0
        num2 = 0
        
        digit = 1
        while l1:
            num1 += l1.val*digit
            digit = digit*10
            l1 = l1.next
        
        digit = 1
        while l2:
            num2 += l2.val*digit
            digit = digit*10
            l2 = l2.next

        result = str(num1+num2)
        output = ListNode(int(result[-1]))
        path = output
        for i in result[-2::-1]:
            path.next = ListNode(int(i))
            path = path.next
        return output
