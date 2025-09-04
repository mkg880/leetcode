class Solution:
    def resultGrid(self, image: List[List[int]], threshold: int) -> List[List[int]]:
        m, n = len(image), len(image[0])
        s = [[0] * n for _ in range(m)]
        num = [[0] * n for _ in range(m)]
        for i in range(m-2):
            for j in range(n-2):
                ma = float('-inf')
                total = 0
                for x in range(3):
                    for y in range(3):
                        if x < 2:
                            ma = max(ma, abs(image[i+x][j+y] - image[i+x+1][j+y]))
                        if y < 2:
                            ma = max(ma, abs(image[i+x][j+y] - image[i+x][j+y+1]))
                        total += image[i+x][j+y]
                if ma <= threshold:
                    avg = total // 9
                    for x in range(3):
                        for y in range(3):
                            s[i+x][j+y] += avg
                            num[i+x][j+y] += 1
        return [[s[i][j] // num[i][j] if num[i][j] > 0 else image[i][j] for j in range(n)] for i in range(m)]