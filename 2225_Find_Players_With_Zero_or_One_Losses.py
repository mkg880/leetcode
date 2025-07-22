class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        m = {}
        zero = set()
        one = set()
        for winner, loser in matches:
            m[winner] = m.get(winner, 0)
            if m[winner] == 0:
                zero.add(winner)
            m[loser] = m.get(loser, 0) + 1
            if m[loser] == 1:
                if loser in zero:
                    zero.remove(loser)
                one.add(loser)
            else:
                if loser in one:
                    one.remove(loser)
        return [sorted(list(zero)), sorted(list(one))]