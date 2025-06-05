"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        res = Node(head.val)
        temp = res
        m = {head: res, None: None}
        temp2 = head.next
        while temp2:
            temp.next = Node(temp2.val)
            temp = temp.next
            m[temp2] = temp
            temp2 = temp2.next
        temp = res
        temp2 = head
        while temp:
            temp.random = m[temp2.random]
            temp = temp.next
            temp2 = temp2.next
        return res
