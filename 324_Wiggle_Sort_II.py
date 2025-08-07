class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        s = sorted(nums)
        n = len(nums)
        mid = ceil(n / 2)
        for i in range(n):
            if i % 2 == 0:
                idx = mid - i // 2 - 1
            else:
                idx = n - i // 2 - 1
            nums[i] = s[idx]