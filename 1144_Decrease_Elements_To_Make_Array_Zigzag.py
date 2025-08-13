class Solution:
    def movesToMakeZigzag(self, nums: List[int]) -> int:
        n = len(nums)
        case1 = 0
        case2 = 0
        for i in range(n):
            d = None
            if i > 0 and nums[i] >= nums[i-1]:
                d = nums[i] - nums[i-1] + 1
            if i+1 < n and nums[i] >= nums[i+1]:
                temp = nums[i] - nums[i+1] + 1
                if d is None or d < temp:
                    d = temp
            if d is not None:
                if i % 2 == 0:
                    case1 += d
                else:
                    case2 += d
        return min(case1, case2)