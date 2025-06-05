# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        def rec(node, h):
            if not node:
                return
            if h < len(res):
                res[h] = node.val
            else:
                res.append(node.val)
            rec(node.left, h+1)
            rec(node.right, h+1)
        rec(root, 0)
        return res