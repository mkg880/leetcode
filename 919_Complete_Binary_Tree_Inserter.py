# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class CBTInserter:

    def __init__(self, root: Optional[TreeNode]):
        self.root = root
        self.q = deque([root])
        while self.q[0].left and self.q[0].right:
            curr = self.q.popleft()
            self.q.append(curr.left)
            self.q.append(curr.right)

    def insert(self, val: int) -> int:
        curr = self.q[0]
        if not curr.left:
            curr.left = TreeNode(val)
            return curr.val
        curr.right = TreeNode(val)
        self.q.popleft()
        self.q.append(curr.left)
        self.q.append(curr.right)
        return curr.val

    def get_root(self) -> Optional[TreeNode]:
        return self.root


# Your CBTInserter object will be instantiated and called as such:
# obj = CBTInserter(root)
# param_1 = obj.insert(val)
# param_2 = obj.get_root()