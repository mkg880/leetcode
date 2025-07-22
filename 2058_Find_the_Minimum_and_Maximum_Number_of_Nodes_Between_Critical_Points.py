# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        minDistance = float('inf')
        maxDistance = float('-inf')
        prev_val = head.val
        head = head.next
        prev_pt = 0
        i = 1
        while head.next:
            next_val = head.next.val
            if (prev_val < head.val and next_val < head.val) or (prev_val > head.val and next_val > head.val):
                if prev_pt:
                    minDistance = min(minDistance, i - prev_pt)
                    maxDistance = max(maxDistance, i - first_pt)
                else:
                    first_pt = i
                prev_pt = i
            i += 1
            prev_val = head.val
            head = head.next
        if minDistance == float('inf'):
            return [-1, -1]
        return [minDistance, maxDistance]