# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        prevEven = None
        prevOdd = None
        startEven = None
        startOdd = None
        temp = head
        odd = True
        while temp:
            if odd:
                if prevOdd:
                    prevOdd.next = temp
                else:
                    startOdd = temp
                    prevOdd = temp
                prevOdd = temp
            else:
                if prevEven:
                    prevEven.next = temp
                else:
                    startEven = temp
                prevEven = temp
            temp = temp.next
            odd = not odd
        prevOdd.next = startEven
        prevEven.next = None
        return startOdd