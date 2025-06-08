# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def traverse(self, root):
        if not root:
            return 0
        self.traverse(root.right)
        self.cnt += root.val
        root.val = self.cnt
        self.traverse(root.left)
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.cnt = 0
        self.traverse(root)
        return root