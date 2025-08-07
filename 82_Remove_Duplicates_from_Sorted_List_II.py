# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = head
        prev = None
        while temp:
            v = temp.val
            n = temp.next
            dup = False
            while n and n.val == v:
                dup = True
                n = n.next
            if not dup:
                prev = temp
                temp = temp.next
            else:
                if prev:
                    prev.next = n
                else:
                    head = n
                temp = n
        return head