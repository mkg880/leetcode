class ContraString:
    def __init__(self, s):
        self.s = s

    def __lt__(self, other):
        return self.s > other.s

    def __eq__(self, other):
        return self.s == other.s
    
    def get_str(self):
        return self.s

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        c = Counter(words)
        heap = []
        for key in c:
            curr = ContraString(key)
            if len(heap) == k:
                 cnt, s = heap[0]
                 if c[key] > cnt or (c[key] == cnt and curr > s):
                     heappop(heap)
            if len(heap) < k:
                heappush(heap, (c[key], curr))
        res = []
        while heap:
            _, s = heappop(heap)
            res.append(s.get_str())
        return res