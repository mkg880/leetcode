# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        def getMiddle(node):
            slow, fast, prev = node, node, None
            while fast and fast.next:
                prev = slow
                slow = slow.next
                fast = fast.next.next
            if prev:
                prev.next = None
            return slow
            
        def rec(node):
            if not node:
                return None
            if not node.next:
                return TreeNode(node.val)
            mid = getMiddle(node)
            ret = TreeNode(mid.val)
            ret.right = rec(mid.next)
            ret.left = rec(node)
            return ret
        return rec(head)