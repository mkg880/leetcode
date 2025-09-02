# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        heights = []
        def fill_arr(node, lvl=0, parent=None):
            if not node:
                return
            if lvl == len(heights):
                heights.append([0, {}])
            heights[lvl][0] += node.val
            heights[lvl][1][parent] = heights[lvl][1].get(parent, 0) + node.val
            fill_arr(node.left, lvl+1, node)
            fill_arr(node.right, lvl+1, node)
        def replace(node, lvl=0, parent=None):
            if not node:
                return
            total, m = heights[lvl]
            node.val = total - m[parent]
            replace(node.left, lvl+1, node)
            replace(node.right, lvl+1, node)
        fill_arr(root)
        replace(root)
        return root