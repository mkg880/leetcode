# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        tail = list2
        while tail.next:
            tail = tail.next
        i = 0
        curr = list1
        while curr:
            if i == a - 1:
                start = curr
            if i == b + 1:
                end = curr
                break
            curr = curr.next
            i += 1
        start.next = list2
        tail.next = end
        return list1