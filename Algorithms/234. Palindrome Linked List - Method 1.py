# Given the head of a singly linked list, return true if it is a palindrome.


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        check = []
        while head:
            check.append(head.val)
            head = head.next
        start, end = 0, len(check)-1
        while start < end:
            if check[start] != check[end]:
                return False
            start += 1
            end -= 1
        return True
