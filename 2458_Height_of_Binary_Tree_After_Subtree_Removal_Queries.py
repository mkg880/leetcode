# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def traverse(self, root, h):
        self.m[root.val] = h
        if not root.left and not root.right:
            self.heights[self.length] = h
            self.l[root.val] = self.length
            self.r[root.val] = self.length
            self.length += 1
        else:
            self.l[root.val] = self.length
            if root.left:
                self.traverse(root.left, h+1)
            if root.right:
                self.traverse(root.right, h+1)
            self.r[root.val] = self.length - 1

    def treeQueries(self, root: Optional[TreeNode], queries: List[int]) -> List[int]:
        self.heights = {}
        self.m = {}
        self.l = {}
        self.r = {}
        self.length = 0
        self.traverse(root, 0)
        n = self.length
        maxl = [0] * n
        maxr = [0] * n
        for i in range(1, n):
            maxl[i] = max(maxl[i-1], self.heights[i-1])
            maxr[n-i-1] = max(maxr[n-i], self.heights[n-i])
        
        res = []
        
        for query in queries:
            maxxl = maxl[self.l[query]]
            maxxr = maxr[self.r[query]]
            res.append(max(max(maxxl, maxxr), self.m[query]-1))
        
        return res