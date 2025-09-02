class Solution:
    def countBlackBlocks(self, m: int, n: int, coordinates: List[List[int]]) -> List[int]:
        res = [0] * 5
        res[0] = (m-1) * (n-1)
        blocks = {}
        for x, y in coordinates:
            for i in range(max(0, x-1), min(x+1, m-1)):
                for j in range(max(0, y-1), min(y+1, n-1)):
                    prev = blocks.get((i, j), 0)
                    res[prev] -= 1
                    res[prev+1] += 1
                    blocks[(i, j)] = prev+1
        return res