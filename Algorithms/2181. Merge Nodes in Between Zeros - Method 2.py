# You are given the head of a linked list, which contains a series of integers separated by 0's. The beginning and end of the linked list will have Node.val == 0.

# For every two consecutive 0's, merge all the nodes lying in between them into a single node whose value is the sum of all the merged nodes. 
# The modified list should not contain any 0's.

# Return the head of the modified linked list.


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head.next
        total = 0

        while fast:
            if fast.val == 0:
                slow = slow.next
                slow.val = total
                total = 0
            else:
                total += fast.val
            fast = fast.next

        slow.next = None
        return head.next
