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
    public int[] nextLargerNodes(ListNode head) {
        ArrayList<Integer> nums = new ArrayList<>();
        while(head != null) {
            ListNode next = head.next;
            int num = 0;
            while(next != null) {
                if(next.val > head.val) {
                    num = next.val;
                    break;
                }
                next = next.next;
            }
            nums.add(num);
            head = head.next;
        }
        int[] result = new int[nums.size()];
        for(int i = 0; i < nums.size(); i++) {
            result[i] = nums.get(i);
        }
        return result;
    }
}