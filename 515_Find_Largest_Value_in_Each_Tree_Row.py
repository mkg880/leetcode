# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        def rec(node, idx):
            if not node:
                return
            if idx == len(res):
                res.append(node.val)
            elif node.val > res[idx]:
                res[idx] = node.val
            rec(node.left, idx+1)
            rec(node.right, idx+1)
        rec(root, 0)
        return res