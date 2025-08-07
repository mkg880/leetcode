class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        stack = [(0, [], 0)]
        while stack:
            i, arr, s = stack.pop()
            if s == target:
                res.append(arr)
                continue
            if i >= len(candidates) or s > target:
                continue
            for j in range(i, len(candidates)):
                if j > i and candidates[j] == candidates[j-1]:
                    continue
                stack.append((j+1, arr + [candidates[j]], s + candidates[j]))
        return res