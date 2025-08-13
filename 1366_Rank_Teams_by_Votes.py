class Solution:
    def rankTeams(self, votes: List[str]) -> str:
        n = len(votes[0])
        m = {c: [0]*n for c in votes[0]}
        for s in votes:
            for i in range(n):
                m[s[i]][i] += 1
        res = sorted(m.items(), key=lambda item: [[-x for x in item[1]], item[0]])
        print(res)
        return ''.join([item[0] for item in res])