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
    public ListNode get(ListNode head, int index) {
        int i = 1;
        while(i < index) {
            i++;
            head = head.next;
        }
        return head;
    }
    public ListNode reverseBetween(ListNode head, int left, int right) {
        for(int i = 0; i < (right - left + 1) / 2; i++) {
            ListNode l = get(head, left + i);
            ListNode r = get(head, right - i);
            int temp = l.val;
            l.val = r.val;
            r.val = temp;
        }
        return head;
    }
}