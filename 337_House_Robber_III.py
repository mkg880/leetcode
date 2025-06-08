# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self, root):
        if root is None:
            return (0, 0)
        l1, l2 = self.helper(root.left)
        r1, r2 = self.helper(root.right)
        return (root.val + l2 + r2, max(l1 + r1, l2 + r2, l1 + r2, l2 + r1))
    def rob(self, root: Optional[TreeNode]) -> int:
        a, b = self.helper(root)
        return max(a, b)
            