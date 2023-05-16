# Given a linked list, swap every two adjacent nodes and return its head. 
# You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def recursive(head):
            if head and head.next:
                cur = recursive(head.next.next)
                temp = head.next
                head.next = cur
                temp.next = head
                return temp
            else:
                return head
        
        return recursive(head)
