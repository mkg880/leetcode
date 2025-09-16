class Solution:
    def maximumPoints(self, enemyEnergies: List[int], currentEnergy: int) -> int:
        n = len(enemyEnergies)
        enemyEnergies.sort()
        r = n-1
        mi = enemyEnergies[0]
        if mi > currentEnergy:
            return 0
        res = 0
        while r >= 0:
            if currentEnergy >= mi:
                cnt = currentEnergy // mi
                res += cnt
                currentEnergy -= mi * cnt
            else:
                currentEnergy += enemyEnergies[r]
                r -= 1
        return res