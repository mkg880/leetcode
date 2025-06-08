# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        res = 0
        def rec(node):
            nonlocal res
            if not node:
                return
            if node.val >= low and node.val <= high:
                res += node.val
                rec(node.left)
                rec(node.right)
            elif node.val >= low:
                rec(node.left)
            elif node.val <= high:
                rec(node.right)
        rec(root)
        return res