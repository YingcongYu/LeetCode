# You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

# Merge all the linked-lists into one sorted linked-list and return it.


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        nodes = []
        heapq.heapify(nodes)
        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(nodes, (lists[i].val, i))
                lists[i] = lists[i].next
        
        output = ListNode(0)
        cur = output

        while nodes:
            node, index = heapq.heappop(nodes)
            cur.next = ListNode(node)
            cur = cur.next
            if lists[index]:
                heapq.heappush(nodes, (lists[index].val, index))
                lists[index] = lists[index].next
        
        return output.next
