# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        m = []
        temp = head
        x = k - 1
        while temp:
            m.append(temp)
            temp = temp.next
        t = m[x].val
        m[x].val = m[-k].val
        m[-k].val = t
        return head