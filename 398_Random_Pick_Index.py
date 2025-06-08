class Solution:

    def __init__(self, nums: List[int]):
        self.m = defaultdict(list)
        for i in range(len(nums)):
            self.m[nums[i]].append(i)

    def pick(self, target: int) -> int:
        return self.m[target][random.randint(0, len(self.m[target]) - 1)]


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)