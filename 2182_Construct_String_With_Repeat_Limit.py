class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        cnt = Counter(s)
        heap = [(-ord(key), cnt[key]) for key in cnt]
        heapify(heap)
        res = ''
        while heap:
            c, amt = heappop(heap)
            c = chr(-c)
            res += c * min(amt, repeatLimit)
            if heap and amt > repeatLimit:
                temp1, temp2 = heappop(heap)
                res += chr(-temp1)
                if temp2 > 1:
                    heappush(heap, (temp1, temp2 - 1))
                heappush(heap, (-ord(c), amt - repeatLimit))
        return res