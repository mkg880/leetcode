"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        arr = []
        def rec(node, level):
            if not node:
                return
            if level == len(arr):
                arr.append([])
            arr[level].append(node)
            rec(node.left, level + 1)
            rec(node.right, level + 1)
        rec(root, 0)
        for row in arr:
            for i in range(len(row) - 1):
                row[i].next = row[i+1]
        return root