# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        parent = {}
        parent[root] = None
        def populate(node):
            if not node:
                return
            if node.left:
                parent[node.left] = node
            if node.right:
                parent[node.right] = node
            populate(node.left)
            populate(node.right)
        populate(root)
        s = set()
        while p:
            s.add(p)
            p = parent[p]
        while q not in s:
            q = parent[q]
        return q