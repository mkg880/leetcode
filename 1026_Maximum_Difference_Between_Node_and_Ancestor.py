# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        res = float('-inf')
        def rec(node, ma, mi):
            nonlocal res
            if not node:
                return
            if ma > float('-inf') and mi < float('inf'):
                res = max(res, abs(ma - node.val), (node.val - mi))
            ma = max(ma, node.val)
            mi = min(mi, node.val)
            rec(node.left, ma, mi)
            rec(node.right, ma, mi)
        rec(root, float('-inf'), float('inf'))
        return res