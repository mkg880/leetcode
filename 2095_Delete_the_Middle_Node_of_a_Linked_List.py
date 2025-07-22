# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head.next:
            return None
        a, b = head, head
        prev = None
        while b and b.next:
            prev = a
            a = a.next
            b = b.next.next
        prev.next = a.next
        return head