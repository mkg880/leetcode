class Solution:
    def maximumProduct(self, nums: List[int], k: int) -> int:
        heapify(nums)
        for _ in range(k):
            val = heappop(nums)
            heappush(nums, val+1)
        prod = 1
        mod = 10 ** 9 + 7
        for val in nums:
            prod *= val
            prod %= mod
        return prod