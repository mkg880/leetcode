class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        def rec(arr, start):
            if not arr:
                return 0
            k = 1
            while k <= len(arr):
                temp = sorted(arr[:k])
                check = [i + start for i in range(k)]
                if temp == check:
                    return 1 + rec(arr[k:], k + start)
                k += 1
            return 0
        return rec(arr, 0)
