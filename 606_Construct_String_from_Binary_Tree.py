# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        res = ''
        def rec(node):
            nonlocal res
            res += str(node.val)
            if node.left:
                res += '('
                rec(node.left)
                res += ')'
            elif node.right:
                res += '()'
            if node.right:
                res += '('
                rec(node.right)
                res += ')'
        rec(root)
        return res