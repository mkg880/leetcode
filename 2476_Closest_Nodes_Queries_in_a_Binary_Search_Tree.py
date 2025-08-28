# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import bisect
class Solution:
    def closestNodes(self, root: Optional[TreeNode], queries: List[int]) -> List[List[int]]:
        arr = []
        def inorder(node):
            if not node:
                return
            nonlocal arr
            inorder(node.left)
            arr.append(node.val)
            inorder(node.right)
        inorder(root)
        res = []
        for q in queries:
            idx = bisect.bisect_left(arr, q)
            if idx < len(arr) and arr[idx] == q:
                res.append([q, q])
            else:
                r = arr[idx] if idx < len(arr) else -1
                l = arr[idx-1] if idx > 0 else -1
                res.append([l, r])
        return res