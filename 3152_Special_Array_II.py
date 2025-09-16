import bisect
class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        parity = nums[0] % 2
        start = 0
        arr = []
        for end in range(1, len(nums)):
            if nums[end] % 2 == parity:
                arr.append([start, end-1])
                start = end
            parity = nums[end] % 2
        arr.append([start, len(nums) - 1])
        res = []
        for a, b in queries:
            idx = bisect.bisect_right(arr, a, key=lambda x : x[0]) - 1
            res.append(idx >= 0 and b <= arr[idx][1])
        return res