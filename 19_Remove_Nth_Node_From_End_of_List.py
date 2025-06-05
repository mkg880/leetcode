# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        ahead = head
        behind = head
        for i in range(n):
            ahead = ahead.next
        if not ahead:
            return head.next
        while ahead.next:
            ahead = ahead.next
            behind = behind.next
        behind.next = behind.next.next
        return head