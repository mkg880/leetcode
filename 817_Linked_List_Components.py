# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def numComponents(self, head: Optional[ListNode], nums: List[int]) -> int:
        s = set(nums)
        res = 0
        temp = head
        while temp:
            if temp.val in s and (not temp.next or temp.next.val not in s):
                res += 1
            temp = temp.next
        return res