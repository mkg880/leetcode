class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        m = {}
        for n in nums:
            if n not in m:
                m[n] = 0
            m[n] += 1
        arr = sorted([key for key in m], key=lambda x : -m[x])
        return arr[:k]