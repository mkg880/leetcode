class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        if len(arr) == k:
            return arr
        l = bisect_left(arr, x)
        if l < len(arr) and arr[l] == x:
            res = [x]
            start = l
        else:
            min_dist, start = float('inf'), None
            if l < len(arr):
                min_dist, start = abs(x - arr[l]), l
            if l > 0:
                dist = abs(x - arr[l-1])
                if dist <= min_dist:
                    min_dist, start = dist, l-1
            res = [arr[start]]
        i, j = start-1, start+1
        while len(res) < k:
            l = abs(arr[i] - x) if i >= 0 else float('inf')
            r = abs(arr[j] - x) if j < len(arr) else float('inf')
            if r < l:
                res.append(arr[j])
                j += 1
            else:
                res = [arr[i]] + res
                i -= 1
        return res
