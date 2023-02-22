# Given the head of a linked list, remove the nth node from the end of the list and return its head.


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        def remove(head, n):
            if not head:
                return head, 1
            
            head.next, cur = remove(head.next, n)
            if cur == n:
                return head.next, cur+1
            else:
                return head, cur+1
        
        return remove(head, n)[0]
