# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        if root1 is None and root2 is None:
            return True
        elif root1 is None or root2 is None:
            return False
        if root1.val != root2.val:
            return False
        r1l = root1.left.val if root1.left is not None else None
        r2l = root2.left.val if root2.left is not None else None
        r1r = root1.right.val if root1.right is not None else None
        r2r = root2.right.val if root2.right is not None else None
        if r1l == r2l and r1r == r2r:
            return self.flipEquiv(root1.left, root2.left) and self.flipEquiv(root1.right, root2.right)
        elif r1l == r2r and r1r == r2l:
            return self.flipEquiv(root1.left, root2.right) and self.flipEquiv(root1.right, root2.left)
        else:
            return False