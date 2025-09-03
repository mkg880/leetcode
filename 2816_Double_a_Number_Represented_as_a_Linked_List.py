# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack = []
        temp = head
        while temp:
            stack.append(temp)
            temp = temp.next
        carry = 0
        while stack:
            top = stack.pop()
            dbl = top.val * 2 + carry
            top.val = dbl % 10
            carry = dbl // 10
        if carry:
            new_head = ListNode(carry, head)
            return new_head
        return head