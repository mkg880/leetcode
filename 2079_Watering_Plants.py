class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        curr = capacity
        steps = 0
        i = 0
        while i < len(plants):
            w = plants[i]
            if w <= curr:
                curr -= w
                i += 1
                steps += 1
            else:
                steps += i * 2
                curr = capacity
        return steps