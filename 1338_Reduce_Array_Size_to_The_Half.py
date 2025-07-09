class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        m = {}
        for val in arr:
            m[val] = m.get(val, 0) + 1
        a = sorted(m.keys(), key=lambda x: -m[x])
        goal = ceil(len(arr) / 2)
        print(goal)
        curr = 0
        for i in range(len(a)):
            curr += m[a[i]]
            if curr >= goal:
                return i + 1