# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        res = 0
        d = 0
        def rec(node, lvl):
            nonlocal res, d
            if not node:
                return
            if not node.left and not node.right:
                if lvl == d:
                    res += node.val
                elif lvl > d:
                    res = node.val
                    d = lvl
            else:
                rec(node.left, lvl+1)
                rec(node.right, lvl+1)
        rec(root, 0)
        return res