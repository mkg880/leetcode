class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        self.arr = [[t, p] for t, p in zip(times, persons)]
        self.pre = []
        m = {}
        max_cnt = 0
        winner = -1
        for p in persons:
            self.pre.append(winner)
            m[p] = m.get(p, 0) + 1
            if m[p] >= max_cnt:
                max_cnt = m[p]
                winner = p
        self.pre.append(winner)
    def q(self, t: int) -> int:
        idx = bisect_right(self.arr, t, key=lambda x: x[0])
        return self.pre[idx]


# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)