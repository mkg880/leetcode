# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        res = 'zzzzzzzzzzzzzzzzzzzzzzzzzzzzzz'
        def rec(r, s):
            nonlocal res
            if not r.left and not r.right and chr(r.val + ord('a')) + s < res:
                res = chr(r.val + ord('a')) + s
            elif r.right and r.left:
                if r.right.val < r.left.val:
                    rec(r.right, chr(r.val + ord('a')) + s)
                    rec(r.left, chr(r.val + ord('a')) + s)
                else:
                    rec(r.left, chr(r.val + ord('a')) + s)
                    rec(r.right, chr(r.val + ord('a')) + s)
            elif r.right:
                rec(r.right, chr(r.val + ord('a')) + s)
            elif r.left:
                rec(r.left, chr(r.val + ord('a')) + s)
        rec(root, '')
        return res
                