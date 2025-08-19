class Solution:
    def bestCoordinate(self, towers: List[List[int]], radius: int) -> List[int]:
        max_qual, coords = float('-inf'), [0, 0]
        for i in range(51):
            for j in range(51):
                quality = 0
                for x, y, q in towers:
                    dist = (abs(x - i) ** 2 + abs(y - j) ** 2) ** 0.5
                    if dist <= radius:
                        quality += q // (1 + dist)
                if quality > max_qual or quality == max_qual and [i, j] < coords:
                    max_qual = quality
                    coords = [i, j]   
        return coords