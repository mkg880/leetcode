# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def rec(node):
            if not node:
                return False
            res = node.val == 1
            if not rec(node.left):
                node.left = None
            else:
                res = True
            if not rec(node.right):
                node.right = None
            else:
                res = True
            return res
        b = rec(root)
        return root if b else None