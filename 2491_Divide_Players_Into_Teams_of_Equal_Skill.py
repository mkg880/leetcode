class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        val = None
        res = 0
        for i in range(len(skill) // 2):
            score = skill[i] + skill[-i-1]
            if val is not None and score != val:
                return -1
            val = score
            res += skill[i] * skill[-i-1]
        return res