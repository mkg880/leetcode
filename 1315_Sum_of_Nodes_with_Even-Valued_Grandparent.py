# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: Optional[TreeNode]) -> int:
        res = 0
        def rec(node, p, g):
            nonlocal res
            if not node:
                return
            if g is not None and g % 2 == 0:
                res += node.val
            rec(node.left, node.val, p)
            rec(node.right, node.val, p)
        rec(root, None, None)
        return res