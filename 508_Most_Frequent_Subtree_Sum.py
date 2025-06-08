# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        m = {}
        def rec(node):
            if not node:
                return 0
            s = node.val + rec(node.left) + rec(node.right)
            m[s] = m.get(s, 0) + 1
            return s
        rec(root)
        highest = 0
        res = []
        for key in m:
            if m[key] > highest:
                highest = m[key]
                res = [key]
            elif m[key] == highest:
                res.append(key)
        return res