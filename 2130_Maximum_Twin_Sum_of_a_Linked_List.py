# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        stack = []
        temp = head
        while temp:
            stack.append(temp.val)
            temp = temp.next
        half = len(stack) / 2
        res = 0
        while len(stack) > half:
            val = stack.pop() + head.val
            res = max(res, val)
            head = head.next
        return res