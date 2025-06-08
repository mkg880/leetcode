# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        neighbors = defaultdict(list)
        def populateNeighbors(node):
            if node.left:
                neighbors[node.left.val].append(node.val)
                neighbors[node.val].append(node.left.val)
                populateNeighbors(node.left)
            if node.right:
                neighbors[node.right.val].append(node.val)
                neighbors[node.val].append(node.right.val)
                populateNeighbors(node.right)
        populateNeighbors(root)
        stack = [[target.val, 0]]
        res = []
        visited = set()
        while stack:
            node, dist = stack.pop()
            if node in visited:
                continue
            visited.add(node)
            if dist == k:
                res.append(node)
                continue
            for neighbor in neighbors[node]:
                stack.append([neighbor, dist + 1])
        return res