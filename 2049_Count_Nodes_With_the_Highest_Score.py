class Solution:
    def countHighestScoreNodes(self, parents: List[int]) -> int:
        n = len(parents)
        children = {i: [] for i in range(n)}
        for i in range(1, n):
            parent = parents[i]
            children[parent].append(i)
        high_score = 0
        cnt = 0
        def rec(node):
            nonlocal high_score, cnt
            score = 1
            ret = 1
            for c in children[node]:
                sub = rec(c)
                ret += sub
                score *= sub
            above = n - ret
            if above:
                score *= above
            if score > high_score:
                high_score = score
                cnt = 1
            elif score == high_score:
                cnt += 1
            return ret
        rec(0)
        return cnt