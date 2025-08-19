class Solution:
    def reinitializePermutation(self, n: int) -> int:
        perm = list(range(n))
        for i in range(n):
            valid = True
            arr = []
            for j in range(n):
                new_val = perm[j // 2] if j % 2 == 0 else perm[n // 2 + (j-1) // 2]
                if new_val != j:
                    valid = False
                arr.append(new_val)
            if valid:
                return i+1
            perm = arr
        return -1