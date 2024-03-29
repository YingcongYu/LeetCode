# Given the head of a singly linked list, return true if it is a palindrome.


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        fast = head
        slow = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        prev = None
        while slow:
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp
        fast = head
        slow = prev
        while slow:
            if fast.val != slow.val:
                return False
            else:
                fast = fast.next
                slow = slow.next
        return True
