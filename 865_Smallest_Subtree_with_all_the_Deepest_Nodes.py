# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        deepest = []
        max_depth = 0
        def rec(node, arr, d):
            nonlocal deepest, max_depth
            if not node:
                return
            temp = arr + [node]
            if d > max_depth:
                max_depth = d
                deepest = [temp]
            elif d == max_depth:
                deepest.append(temp)
            rec(node.left, temp, d+1)
            rec(node.right, temp, d+1)
        rec(root, [], 1)
        if not deepest:
            return None
        for i in range(max_depth - 1, -1, -1):
            val = deepest[0][i]
            valid = True
            for arr in deepest[1:]:
                if arr[i] != val:
                    valid = False
                    break
            if valid:
                return val
            