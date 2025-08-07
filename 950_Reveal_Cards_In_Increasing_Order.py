class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        n = len(deck)
        deck.sort()
        res = [0] * n
        q = deque(range(n))
        i = 0
        while q:
            res[q.popleft()] = deck[i]
            i += 1
            if q:
                q.append(q.popleft())
        return res