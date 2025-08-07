# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None
        temp = head
        n = 0
        while temp:
            temp = temp.next
            n += 1
        k %= n
        if not k:
            return head
        new_tail = head
        cnt = 0
        while cnt < n-k-1:
            cnt += 1
            new_tail = new_tail.next
        new_head = new_tail.next
        new_tail.next = None
        temp = new_head
        while temp.next:
            temp = temp.next
        temp.next = head
        return new_head