# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        res = ListNode()
        temp = res
        carry = 0
        moved = False
        while l1 or l2 or carry:
            a = l1.val if l1 else 0
            b = l2.val if l2 else 0
            s = a + b + carry
            carry = s // 10
            if moved:
                temp.next = ListNode()
                temp = temp.next
            temp.val += s % 10
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
            moved = True
        return res