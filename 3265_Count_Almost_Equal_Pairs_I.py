from typing import Counter
class Solution:
    def countPairs(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0
        for i in range(n):
            for j in range(i+1, n):
                s1 = str(nums[i])
                x = len(s1)
                s2 = str(nums[j])
                y = len(s2)
                l = max(x, y)
                while x < l:
                    s1 = '0' + s1
                    x += 1
                while y < l:
                    s2 = '0' + s2
                    y += 1
                c1, c2 = Counter(s1), Counter(s2)
                d = sum(s1[i] != s2[i] for i in range(l))
                if c1 == c2 and d <= 2:
                    res += 1
        return res