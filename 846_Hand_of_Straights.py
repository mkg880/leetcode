class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        hand.sort()
        m = {}
        for i in hand:
            if i not in m:
                m[i] = 1
            else:
                m[i] += 1
        for i, j in m.items():
            if j < 1:
                continue
            for k in range(i+1, i + groupSize):
                if k not in m or m[k] < j:
                    return False
            for k in range(i, i + groupSize):
                m[k] -= j
        return True