# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        m = {}
        def traverse(root, level):
            if not root:
                return
            if level not in m:
                m[level] = 0
            m[level] += root.val
            traverse(root.left, level + 1)
            traverse(root.right, level + 1)
        traverse(root, 0)
        arr = sorted(m.items(), key=lambda item: -item[1])
        if len(arr) < k:
            return -1
        return arr[k-1][1]