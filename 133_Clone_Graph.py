"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not Node:
            return None
        stack = [node]
        m = {}
        while stack:
            curr = stack.pop()
            if not curr or curr.val in m:
                continue
            copy = Node(curr.val)
            m[curr.val] = copy
            for n in curr.neighbors:
                stack.append(n)
        stack.append(node)
        visited = set()
        while stack:
            curr = stack.pop()
            if not curr or curr.val in visited:
                continue
            for n in curr.neighbors:
                m[curr.val].neighbors.append(m[n.val])
                stack.append(n)
            visited.add(curr.val)
        return m[1] if m else None