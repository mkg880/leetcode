class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        n = len(accounts)
        id = list(range(n))

        def find(p):
            while p != id[p]:
                p = id[p]
            return p

        def union(p, q):
            idP = find(p)
            idQ = find(q)
            id[idP] = idQ

        m = {}
        for i in range(n):
            for email in accounts[i][1:]:
                if email in m:
                    union(i, m[email])
                else:
                    m[email] = i
        
        groups = {}
        for x in range(n):
            idx = find(x)
            if idx not in groups:
                groups[idx] = []
            groups[idx].append(x)
        
        res = []
        for key in groups:
            curr = [accounts[key][0]]
            s = set()
            for i in groups[key]:
                s.update(set(accounts[i][1:]))
            curr += sorted(list(s))
            res.append(curr)
        return res