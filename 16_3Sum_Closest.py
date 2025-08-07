class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        diff = float('inf')
        res = -1
        nums.sort()
        n = len(nums)
        for i in range(n):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l, r = i+1, n-1
            while l < r:
                curr = nums[i] + nums[l] + nums[r]
                if curr == target:
                    return curr
                elif curr < target:
                    if target - curr < diff:
                        diff = target - curr
                        res = curr
                    l += 1
                else:
                    if curr - target < diff:
                        diff = curr - target
                        res = curr
                    r -= 1
        return res