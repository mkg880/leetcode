"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        node = Node(head.val, None, None, None)
        temp = node
        def add(n):
            nonlocal temp
            if not n:
                return
            temp.next = Node(n.val, temp, None, None)
            temp = temp.next
            add(n.child)
            add(n.next)
        add(head.child)
        add(head.next)
        return node