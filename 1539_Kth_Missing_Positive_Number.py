class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        curr = 1
        for val in arr:
            diff = val - curr
            if diff == 0:
                curr += 1
            elif diff >= k:
                return curr + k - 1
            else:
                k -= diff
                curr = val + 1
        return curr + k - 1