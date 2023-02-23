# Given the head of a linked list, return the list after sorting it in ascending order.


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        nodes = []
        cur = head
        while cur:
            nodes.append(cur.val)
            cur = cur.next
        
        nodes.sort()
        cur = head
        for i in nodes:
            cur.val = i
            cur = cur.next
        
        return head
