# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        nodes = []
        temp = head
        while temp:
            nodes.append(temp)
            temp = temp.next
        n = len(nodes)
        dummy = ListNode()
        prev = dummy
        for i in range(0, n, 2):
            if i+1 < n:
                prev.next = nodes[i+1]
                nodes[i+1].next = nodes[i]
                prev = nodes[i]
                nodes[i].next = None
            else:
                prev.next = nodes[i]
        return dummy.next