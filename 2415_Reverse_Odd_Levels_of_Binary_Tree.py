# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        m = {}
        def first(root, level):
            if not root:
                return
            if level % 2 == 1:
                if level not in m:
                    m[level] = []
                m[level].append(root.val)
            first(root.left, level + 1)
            first(root.right, level + 1)
        def second(root, level):
            if not root:
                return
            if level % 2 == 1:
                root.val = m[level].pop()
            second(root.left, level + 1)
            second(root.right, level + 1)
        first(root, 0)
        second(root, 0)
        return root