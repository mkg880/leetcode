# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> List[int]:
        def inorder(node):
            if not node:
                return []
            return inorder(node.left) + [node.val] + inorder(node.right)
        a, b = inorder(root1), inorder(root2)
        print(a, b)
        i, j = 0, 0
        res = []
        while i < len(a) or j < len(b):
            x = a[i] if i < len(a) else float('inf')
            y = b[j] if j < len(b) else float('inf')
            if x <= y:
                res.append(x)
                i += 1
            else:
                res.append(y)
                j += 1
        return res