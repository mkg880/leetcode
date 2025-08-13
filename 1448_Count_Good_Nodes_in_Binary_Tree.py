# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = 0
        def rec(node, max_val):
            nonlocal res
            if not node:
                return
            if node.val >= max_val:
                res += 1
                max_val = node.val
            rec(node.left, max_val)
            rec(node.right, max_val)
        rec(root, float('-inf'))
        return res