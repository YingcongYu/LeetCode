# Given the head of a singly linked list, group all the nodes with odd indices together followed by the nodes with even indices, and return the reordered list.

# The first node is considered odd, and the second node is even, and so on.

# Note that the relative order inside both the even and odd groups should remain as it was in the input.

# You must solve the problem in O(1) extra space complexity and O(n) time complexity.


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        even = ListNode(0)
        cur_even = even
        odd = ListNode(0)
        cur_odd = odd
        index = 1
        
        while head:
            if index % 2 == 1:
                temp = head.next
                head.next = None
                cur_odd.next = head
                cur_odd = cur_odd.next
                head = temp
            else:
                temp = head.next
                head.next = None
                cur_even.next = head
                cur_even = cur_even.next
                head = temp
            index += 1
        
        cur_odd.next = even.next
        return odd.next
