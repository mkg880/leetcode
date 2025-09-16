class Solution:
    def occurrencesOfElement(self, nums: List[int], queries: List[int], x: int) -> List[int]:
        indices = [i for i in range(len(nums)) if nums[i] == x]
        return [indices[q-1] if q <= len(indices) else -1 for q in queries]