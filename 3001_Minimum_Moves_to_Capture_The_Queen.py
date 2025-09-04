class Solution:
    def minMovesToCaptureTheQueen(self, a: int, b: int, c: int, d: int, e: int, f: int) -> int:
        rook = (a == e and (c != a or not (b < d < f or f < d < b))) or (b == f and (d != b or not (a < c < e or e < c < a)))
        d1, d2, d3 = b-a, d-c, f-e
        s1, s2, s3 = b+a, d+c, f+e
        bishop = (d2 == d3 and (d1 != d2 or not (c < a < e or e < a < c))) or (s2 == s3 and (s1 != s2 or not (c < a < e or e < a < c)))
        return 1 if rook or bishop else 2