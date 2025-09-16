from collections import deque
class Solution:
    def findWinningPlayer(self, skills: List[int], k: int) -> int:
        n = len(skills)
        if k >= n:
            return max(range(n), key=lambda x: skills[x])
        wins = 0
        q = deque(range(1, n))
        prev = 0
        while True:
            opp = q.popleft()
            if skills[prev] > skills[opp]:
                wins += 1
                if wins == k:
                    return prev
                q.append(opp)
            else:
                wins = 1
                if wins == k:
                    return opp
                q.append(prev)
                prev = opp