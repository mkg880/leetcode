# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        def rec(node, parent):
            nonlocal root
            if not node:
                return
            if node.val < low:
                if not parent:
                    root = node.right
                else:
                    parent.left = node.right
                rec(node.right, parent)
            elif node.val > high:
                if not parent:
                    root = node.left
                else:
                    parent.right = node.left
                rec(node.left, parent)
            else:
                rec(node.left, node)
                rec(node.right, node)
        rec(root, None)
        return root