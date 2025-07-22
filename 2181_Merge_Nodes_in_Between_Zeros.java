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
    public ListNode mergeNodes(ListNode head) {
        ListNode temp = head;
        ListNode temp2 = head.next;
        while(true) {
            int sum = 0;
            while(temp2.val != 0) {
                sum += temp2.val;
                temp2 = temp2.next;
            }
            temp.val = sum;
            temp.next = temp2;
            if(temp2.next == null) {
                temp.next = null;
                return head;
            }
            temp = temp2;
            temp2 = temp.next;
        }

    }
}