"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        res = []
        def rec(node, level):
            if not root:
                return
            if level == len(res):
                res.append([])
            res[level].append(node.val)
            for child in node.children:
                rec(child, level + 1)
        rec(root, 0)
        return res