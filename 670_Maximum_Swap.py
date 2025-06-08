class Solution:
    def maximumSwap(self, num: int) -> int:
        arr = [c for c in str(num)]
        for i in range(len(arr)):
            m = arr[i]
            idx = i
            for j in range(len(arr) - 1, i, -1):
                if arr[j] > m:
                    idx = j
                    m = arr[j]
            if idx != i:
                arr[i], arr[idx] = arr[idx], arr[i]
                return int("".join(arr))
        return num