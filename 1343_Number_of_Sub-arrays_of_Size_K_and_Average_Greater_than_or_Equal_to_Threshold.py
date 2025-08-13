class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        target = threshold * k
        i, j = 0, 0
        total = 0
        while j < k:
            total += arr[j]
            j += 1
        res = 0 if total < target else 1
        for i in range(len(arr) - k):
            total -= arr[i]
            total += arr[i+k]
            res += 0 if total < target else 1
        return res