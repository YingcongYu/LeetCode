# Given a singly linked list, return a random node's value from the linked list. Each node must have the same probability of being chosen.

# Implement the Solution class:

# Solution(ListNode head) Initializes the object with the head of the singly-linked list head.
# int getRandom() Chooses a node randomly from the list and returns its value. All the nodes of the list should be equally likely to be chosen.


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    import random
    def __init__(self, head: Optional[ListNode]):
        length = 0
        cur = head
        while cur:
            cur = cur.next
            length += 1
        self.length = length
        self.head = head

    def getRandom(self) -> int:
        num = random.randint(0, self.length-1)
        cur = self.head
        while num > 0:
            cur = cur.next
            num -= 1
        return cur.val


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()
