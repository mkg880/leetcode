# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        def rec(node, d):
            if not node:
                return
            if d == depth - 1:
                l = node.left
                r = node.right
                node.left = TreeNode(val, left=l)
                node.right = TreeNode(val, right=r)
            else:
                rec(node.left, d+1)
                rec(node.right, d+1)
        if depth == 1:
            res = TreeNode(val, left=root)
            return res
        rec(root, 1)
        return root