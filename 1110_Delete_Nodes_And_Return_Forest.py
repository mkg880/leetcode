# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        def rec(n, parent, direction):
            if not n:
                return []
            res = []
            l = rec(n.left, n, 'l')
            r = rec(n.right, n, 'r')
            for node in l:
                res.append(node)
            for node in r:
                res.append(node)
            if n.val in to_delete:
                if n.left:
                    res.append(n.left)
                if n.right:
                    res.append(n.right)
                if parent:
                    if direction == 'r':
                        parent.right = None
                    else:
                        parent.left = None
            return res
        if root.val in to_delete:
            return rec(root, None, None)
        return [root] + rec(root, None, None)