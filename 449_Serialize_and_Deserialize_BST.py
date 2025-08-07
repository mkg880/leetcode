# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root: Optional[TreeNode]) -> str:
        """Encodes a tree to a single string.
        """
        arr = []
        q = deque([root])
        while q:
            node = q.popleft()
            if not node:
                arr.append('N')
                continue
            arr.append(str(node.val))
            q.append(node.left)
            q.append(node.right)
        return ','.join(arr)


    def deserialize(self, data: str) -> Optional[TreeNode]:
        """Decodes your encoded data to tree.
        """
        if data == 'N':
            return None
        nodes = data.split(',')
        root = TreeNode(int(nodes[0]))
        q = deque([[root, 0]])
        for i in range(1, len(nodes)):
            if nodes[i] == 'N':
                curr = None
            else:
                curr = TreeNode(int(nodes[i]))
            if q[0][1] == 0:
                q[0][0].left = curr
                q[0][1] = 1
            else:
                q[0][0].right = curr
                q.popleft()
            if curr:
                q.append([curr, 0])
        return root

# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans