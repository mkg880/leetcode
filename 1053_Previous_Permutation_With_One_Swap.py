class Solution:
    def prevPermOpt1(self, arr: List[int]) -> List[int]:
        n = len(arr)
        for i in range(n-2, -1, -1):
            if arr[i] > arr[i+1]:
                max_val, idx = float('-inf'), -1
                for j in range(i+1, n):
                    if arr[i] > arr[j] > max_val:
                        max_val, idx = arr[j], j
                arr[i], arr[idx] = arr[idx], arr[i]
                return arr
        return arr