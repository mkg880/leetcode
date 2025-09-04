class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        n = len(nums)
        id = list(range(n))
        arr = sorted((val, i) for i, val in enumerate(nums))
        prev = arr[0]
        min_vals = {prev[1]: [[prev[0]], 0]}
        for val, i in arr[1:]:
            if val - prev[0] <= limit:
                id[i] = id[prev[1]]
                min_vals[id[i]][0].append(val)
            else:
                min_vals[i] = [[val], 0]
            prev = (val, i)
        res = []
        for i in range(n):
            arr, idx = min_vals[id[i]]
            res.append(arr[idx])
            min_vals[id[i]][1] += 1
        return res