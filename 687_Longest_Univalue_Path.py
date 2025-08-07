# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        res = 0
        def rec(node, parent):
            nonlocal res
            if not node:
                return 0
            l = rec(node.left, node.val)
            r = rec(node.right, node.val)
            res = max(res, l+r)
            if node.val == parent:
                return max(l, r) + 1
            return 0 
        rec(root, None)
        return res