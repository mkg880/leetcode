class Solution:
    def minimumTeachings(self, n: int, languages: List[List[int]], friendships: List[List[int]]) -> int:
        m = {i+1: set() for i in range(n)}
        l_set = [set(l) for l in languages]
        for a, b in friendships:
            if l_set[a-1] & l_set[b-1]:
                continue
            for i in range(1, n+1):
                if i not in l_set[a-1]:
                    m[i].add(a)
                if i not in l_set[b-1]:
                    m[i].add(b)
        res = len(languages)
        for key in m:
            res = min(len(m[key]), res)
        return res