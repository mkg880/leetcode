class Solution:
    def countLargestGroup(self, n: int) -> int:
        largest = 0
        cnt = 0
        m = {}
        for val in range(1, n+1):
            s = 0
            while val != 0:
                s += val % 10
                val = val // 10
            x = m.get(s, 0) + 1
            m[s] = x
            if x == largest:
                cnt += 1
            if x > largest:
                largest = x
                cnt = 1
        return cnt