# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None
        def insert(head, node):
            if not node:
                return
            if node.val < head.val:
                if not head.left:
                    head.left = node
                else:
                    insert(head.left, node)
            else:
                if not head.right:
                    head.right = node
                else:
                    insert(head.right, node)
        def rec(node, parent, d):
            nonlocal root
            if not node:
                return
            if key < node.val:
                rec(node.left, node, 'l')
            elif key > node.val:
                rec(node.right, node, 'r')
            else:
                if not parent and not node.left and not node.right:
                    return 'None'
                elif not node.left and not node.right:
                    if d == 'l':
                        parent.left = None
                    else:
                        parent.right = None
                elif node.left:
                    if not parent:
                        root = node.left
                    elif d == 'l':
                        parent.left = node.left
                    else:
                        parent.right = node.left
                    insert(node.left, node.right)
                else:
                    if not parent:
                        root = node.right
                    elif d == 'l':
                        parent.left = node.right
                    else:
                        parent.right = node.right
                    insert(node.right, node.left)
        if rec(root, None, '') == 'None':
            return None
        return root