// You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

// Merge all the linked-lists into one sorted linked-list and return it.


/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode mergeKLists(ListNode[] lists) {
        Queue<ListNode> nodes = new PriorityQueue<>((n1, n2) -> {return n1.val - n2.val;});
        for (int i = 0; i < lists.length; i++) {
            if (lists[i] != null) {
                nodes.add(lists[i]);
                lists[i] = lists[i].next;
            }
        }

        ListNode output = new ListNode(0);
        ListNode cur = output;

        while (!nodes.isEmpty()) {
            ListNode node = nodes.poll();
            cur.next = node;
            cur = cur.next;
            node = node.next;

            if (node != null) {
                nodes.add(node);
            }
        }

        return output.next;
    }
}
