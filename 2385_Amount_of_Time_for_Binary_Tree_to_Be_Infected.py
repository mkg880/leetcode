# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict, deque
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        graph = defaultdict(list)
        def rec(node):
            if node.left:
                graph[node.val].append(node.left.val)
                graph[node.left.val].append(node.val)
                rec(node.left)
            if node.right:
                graph[node.val].append(node.right.val)
                graph[node.right.val].append(node.val)
                rec(node.right)
        rec(root)
        q = deque([(start, 0)])
        vis = set()
        res = 0
        while q:
            node, d = q.popleft()
            if node in vis:
                continue
            vis.add(node)
            res = max(res, d)
            q.extend([(neighbor, d+1) for neighbor in graph[node]])
        return res