# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        def rec(node):
            if not node:
                return False
            if not rec(node.left):
                node.left = None
            if not rec(node.right):
                node.right = None
            if not node.left and not node.right and node.val == target:
                return False
            return True
        return root if rec(root) else None