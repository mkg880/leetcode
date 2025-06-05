# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        def rec(node, level):
            if not node:
                return
            if level == len(res):
                res.insert(0, [node.val])
            else:
                res[-(level + 1)].append(node.val)
            rec(node.left, level+1)
            rec(node.right, level+1)
        rec(root, 0)
        return res