# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = {}
        curr = head
        p = None
        while curr:
            prev[curr] = p
            p = curr
            curr = curr.next
        curr = p
        nex = None
        max_val = float('-inf')
        while curr:
            if curr.val >= max_val:
                curr.next = nex
                nex = curr
                max_val = curr.val
            curr = prev[curr]
        return nex