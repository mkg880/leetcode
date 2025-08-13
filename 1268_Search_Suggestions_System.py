import bisect
class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        res = []
        products.sort()
        start = 0
        for i in range(len(searchWord)):
            arr = []
            pre = searchWord[:i+1]
            start = bisect.bisect_left(products, pre, key=lambda x: x[:i+1], lo=start)
            j = start
            while j < min(start+3, len(products)) and products[j][:i+1] == pre:
                arr.append(products[j])
                j += 1
            res.append(arr)
        return res