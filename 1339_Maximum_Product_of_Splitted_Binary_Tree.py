# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        total = 0
        def get_total(node):
            nonlocal total
            if not node:
                return
            total += node.val
            get_total(node.left)
            get_total(node.right)
        
        get_total(root)
        res = 0
        def rec(node):
            nonlocal res
            if not node:
                return 0
            val = node.val + rec(node.left) + rec(node.right)
            res = max(res, (total - val) * val)
            return val
        rec(root)
        mod = 10 ** 9 + 7
        return res % mod