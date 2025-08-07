"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        def rec(x, y, n):
            last = grid[x][y]
            valid = True
            for i in range(x, x+n):
                for j in range(y, y+n):
                    if grid[i][j] != last:
                        valid = False
                        break
                if not valid:
                    break
            if valid:
                return Node(True if last else False, True, None, None, None, None)
            ret = Node(False, False, None, None, None, None)
            ret.topLeft = rec(x, y, n // 2)
            ret.topRight = rec(x, y + n // 2, n // 2)
            ret.bottomLeft = rec(x + n // 2, y, n // 2)
            ret.bottomRight = rec(x + n // 2, y + n // 2, n // 2)
            return ret
        return rec(0, 0, len(grid))