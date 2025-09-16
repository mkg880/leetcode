# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        prev, temp = None, head
        s = set(nums)
        while temp:
            if temp.val in s:
                if prev is None:
                    head = temp.next
                else:
                    prev.next = temp.next
            else:
                prev = temp
            temp = temp.next
        return head