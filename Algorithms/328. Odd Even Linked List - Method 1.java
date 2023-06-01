// Given the head of a singly linked list, group all the nodes with odd indices together followed by the nodes with even indices, and return the reordered list.

// The first node is considered odd, and the second node is even, and so on.

// Note that the relative order inside both the even and odd groups should remain as it was in the input.

// You must solve the problem in O(1) extra space complexity and O(n) time complexity.


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
    public ListNode oddEvenList(ListNode head) {
        ListNode even = new ListNode(0);
        ListNode cur_even = even;
        ListNode odd = new ListNode(0);
        ListNode cur_odd = odd;
        int index = 1;
  
        while (head != null) {
            if (index % 2 == 0) {
                ListNode temp = head.next;
                head.next = null;
                cur_even.next = head;
                cur_even = cur_even.next;
                head = temp;
            } else {
                ListNode temp = head.next;
                head.next = null;
                cur_odd.next = head;
                cur_odd = cur_odd.next;
                head = temp;
            }
            index += 1;
        }

        cur_odd.next = even.next;
        return odd.next;
    }
}
