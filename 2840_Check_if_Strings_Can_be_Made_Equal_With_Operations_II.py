class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
        even1, odd1, even2, odd2 = {}, {}, {}, {}
        for i, (a, b) in enumerate(zip(s1, s2)):
            if i % 2 == 0:
                even1[a] = even1.get(a, 0) + 1
                even2[b] = even2.get(b, 0) + 1
            else:
                odd1[a] = odd1.get(a, 0) + 1
                odd2[b] = odd2.get(b, 0) + 1
        return even1 == even2 and odd1 == odd2