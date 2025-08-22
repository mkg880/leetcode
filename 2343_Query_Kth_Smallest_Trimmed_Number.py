class Solution:
    def smallestTrimmedNumbers(self, nums: List[str], queries: List[List[int]]) -> List[int]:
        return [sorted([(s[-trim:], i) for i, s in enumerate(nums)])[k-1][1] for k, trim in queries]