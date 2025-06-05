# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        res = 0
        def rec(node, s):
            nonlocal res
            if not node:
                return
            s += str(node.val)
            if not node.left and not node.right:
                res += int(s)
            else:
                rec(node.left, s)
                rec(node.right, s)
        rec(root, "")
        return res