class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        res = []
        n = len(arr)
        for i in range(n, 0, -1):
            idx = arr.index(i)
            if idx == i-1:
                continue
            if idx > 0:
                res.append(idx+1)
            res.append(i)
            arr = arr[idx+1:i][::-1] + arr[:idx] + [i] + arr[i:]
        return res