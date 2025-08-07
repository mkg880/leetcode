# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        subtrees = set()
        res = []
        done = set()
        def rec(node):
            if not node:
                return '/'
            s = ','.join([str(node.val), rec(node.left), rec(node.right)])
            if s in subtrees:
                if s not in done:
                    res.append(node)
                    done.add(s)
            else:
                subtrees.add(s)
            return s
        rec(root)
        return res