# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        s_path = ''
        t_path = ''
        def rec(node, a):
            nonlocal s_path, t_path
            if not node:
                return
            if node.val == startValue:
                s_path = ''.join(a)
                if t_path:
                    return
            if node.val == destValue:
                t_path = ''.join(a)
                if s_path:
                    return
            a.append('L')
            rec(node.left, a)
            a.pop()
            a.append('R')
            rec(node.right, a)
            a.pop()
        rec(root, [])
        i = 0
        while i < len(s_path) and i < len(t_path) and s_path[i] == t_path[i]:
            i += 1
        return 'U' * (len(s_path) - i) + t_path[i:]