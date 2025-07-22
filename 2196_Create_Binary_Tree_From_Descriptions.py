# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        m = {}
        children = set([d[1] for d in descriptions])
        for parent, child, left in descriptions:
            if parent not in m:
                m[parent] = TreeNode(parent)
            if child not in m:
                m[child] = TreeNode(child)
            if left:
                m[parent].left = m[child]
            else:
                m[parent].right = m[child]
            if parent not in children:
                root = m[parent]
        return root