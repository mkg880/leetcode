# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.stack = []
        def rec(node):
            if not node:
                return
            rec(node.right)
            self.stack.append(node.val)
            rec(node.left)
        rec(root)

    def next(self) -> int:
        return self.stack.pop()

    def hasNext(self) -> bool:
        return bool(self.stack)


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()