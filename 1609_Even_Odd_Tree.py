# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        q = deque([(root, 0)])
        curr = 0
        prev = None
        while q:
            node, lvl = q.popleft()
            if not node:
                continue
            if lvl != curr:
                curr = lvl
                prev = None
            if (lvl % 2 == 0 and (node.val % 2 == 0 or (prev and node.val <= prev))) or (lvl % 2 == 1 and (node.val % 2 == 1 or (prev and node.val >= prev))):
                return False
            prev = node.val
            q.append((node.left, lvl + 1))
            q.append((node.right, lvl + 1))
        return True