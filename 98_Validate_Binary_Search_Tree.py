# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def rec(node, upper, lower):
            if not node:
                return True
            if node.val >= upper or node.val <= lower:
                return False
            return rec(node.left, min(upper, node.val), lower) and rec(node.right, upper, max(lower, node.val))
        return rec(root, float('inf'), float('-inf'))