# Given the head of a linked list and an integer val, remove all the nodes of the linked list that has Node.val == val, and return the new head.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if head is None:
            return head
        dummy = cur = ListNode(0)
        while head:
            if head.val == val and head.next is not None:
                head = head.next
            elif head.val == val and head.next is None:
                head = None
                cur.next = head
            else:
                cur.next = head
                head = head.next
                cur = cur.next
        return dummy.next
