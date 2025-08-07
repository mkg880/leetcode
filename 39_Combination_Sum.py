class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        stack = [(0, [], 0)]
        while stack:
            i, arr, s = stack.pop()
            if i >= len(candidates) or s > target:
                continue
            if s == target:
                res.append(arr)
                continue
            stack.append((i, arr + [candidates[i]], s + candidates[i]))
            stack.append((i+1, arr, s))
        return res