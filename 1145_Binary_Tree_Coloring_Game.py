# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def btreeGameWinningMove(self, root: Optional[TreeNode], n: int, x: int) -> bool:
        l, r = None, None
        def cnt(node):
            nonlocal l, r
            if not node:
                return 0
            if node.val == x:
                l, r = node.left, node.right
                return 0
            return 1 + cnt(node.left) + cnt(node.right)
        return cnt(root) >= n / 2 or cnt(l) >= n / 2 or cnt(r) >= n / 2