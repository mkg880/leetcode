# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def search(self, root, h):
        if not root:
            return
        if h > self.m:
            self.res = root.val
            self.m = h
        self.search(root.left, h+1)
        self.search(root.right, h+1)
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        self.m = -1
        self.search(root, 0)
        return self.res