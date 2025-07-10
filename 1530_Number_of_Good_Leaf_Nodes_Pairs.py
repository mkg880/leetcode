# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countPairs(self, root: Optional[TreeNode], distance: int) -> int:
        parents = {}
        leaves = []
        def populate(node):
            leaf = True
            if node.left:
                parents[node.left] = node
                populate(node.left)
                leaf = False
            if node.right:
                parents[node.right] = node
                populate(node.right)
                leaf = False
            if leaf:
                leaves.append(node)
        populate(root)
        res = 0
        for leaf in leaves:
            stack = [(leaf, 0)]
            visited = set()
            while stack:
                node, dist = stack.pop()
                if node in visited or dist > distance:
                    continue
                visited.add(node)
                if node != leaf and not node.left and not node.right:
                    res += 1
                if node.left:
                    stack.append((node.left, dist + 1))
                if node.right:
                    stack.append((node.right, dist + 1))
                if node in parents:
                    stack.append((parents[node], dist + 1))
        return res // 2