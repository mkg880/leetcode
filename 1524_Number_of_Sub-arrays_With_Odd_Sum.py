class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        evens, odds = 1, 0
        res = 0
        mod = 10**9 + 7
        acc = 0
        for num in arr:
            acc += num
            if acc % 2 == 0:
                res += odds
                evens += 1
            else:
                res += evens
                odds += 1
        return res % mod