# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        temp = head.next
        stack = []
        while temp:
            stack.append(temp)
            temp = temp.next
        end = 1
        temp = head
        while len(stack) > 0:
            toAdd = stack.pop() if end == 1 else stack.pop(0)
            temp.next = toAdd
            temp = temp.next
            end *= -1
        temp.next = None
        return head