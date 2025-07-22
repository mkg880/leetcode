class Solution:
    def countCollisions(self, directions: str) -> int:
        n = len(directions)
        i = 0
        while i < n and directions[i] == 'L':
            i += 1
        if i == n:
            return 0
        j = n - 1
        while j >= 0 and directions[j] == 'R':
            j -= 1
        if j < 0:
            return 0
        res = 0
        for x in range(i, j+1):
            if directions[x] != 'S':
                res += 1
        return res