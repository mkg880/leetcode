# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        res = ListNode()
        while head:
            temp = head.next
            head.next = res.next
            res.next = head
            head = temp
        return res.next