# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        res = 0
        def rec(node, pre, s):
            nonlocal res
            if not node:
                return
            s += node.val
            if s == targetSum:
                res += 1
            diff = s - targetSum
            if diff in pre:
                res += pre[diff]
            pre[s] = pre.get(s, 0) + 1
            rec(node.left, pre, s)
            rec(node.right, pre, s)
            pre[s] -= 1
        rec(root, {}, 0)
        return res