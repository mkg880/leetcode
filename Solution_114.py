# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def append(self, root, to_add):
        if not to_add or not root:
            return
        temp = root
        while temp.right:
            temp = temp.right
        temp.right = to_add

    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return
        r = root.right
        root.right = root.left
        root.left = None
        self.flatten(root.right)
        self.flatten(r)
        self.append(root, r)