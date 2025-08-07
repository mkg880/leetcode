class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        def twoSum(nums, target):
            n = len(nums)
            l, r = 0, n-1
            res = []
            while l < r:
                curr = nums[l] + nums[r]
                if curr == target:
                    res.append([nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                elif curr < target:
                    l += 1
                else:
                    r -= 1
            return res
        def kSum(nums, target, k):
            if k == 2:
                return twoSum(nums, target)
            res = []
            n = len(nums)
            for i in range(n):
                if i > 0 and nums[i] == nums[i-1]:
                    continue
                arr = kSum(nums[i+1:], target - nums[i], k-1)
                for a in arr:
                    a.append(nums[i])
                    res.append(a)
            return res
        nums.sort()
        return kSum(nums, target, 4)