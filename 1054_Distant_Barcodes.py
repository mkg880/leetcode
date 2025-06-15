class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        res = []
        heap = []
        m = {}
        for val in barcodes:
            m[val] = m.get(val, 0) + 1
        for key in m:
            heappush(heap, (-m[key], key))
        amt, val = heappop(heap)
        while heap:
            res.append(val)
            old_amt, old_val = amt + 1, val
            amt, val = heappop(heap)
            if old_amt < 0:
                heappush(heap, (old_amt, old_val))
        res.append(val)
        return res
        