class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        properties.sort(key=lambda x: [-x[0], x[1]])
        curr_max = float('-inf')
        res = 0
        for _, defense in properties:
            if curr_max > defense:
                res += 1
            curr_max = max(curr_max, defense)
        return res