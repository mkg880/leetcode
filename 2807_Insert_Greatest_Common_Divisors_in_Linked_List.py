# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = head
        while temp.next:
            temp.next = ListNode(gcd(temp.val, temp.next.val), temp.next)
            temp = temp.next.next
        return head