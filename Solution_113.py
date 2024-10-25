# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def find(self, root, cnt, arr):
        if not root:
            return
        cnt += root.val
        new_arr = arr + [root.val]
        if not root.left and not root.right and cnt == self.target:
            self.res.append(new_arr)
        else:
            self.find(root.left, cnt, new_arr)
            self.find(root.right, cnt, new_arr)
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        self.target = targetSum
        self.res = []
        self.find(root, 0, [])
        return self.res
        