class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        i = 0
        m = {}
        for val in arr2:
            if val in m:
                continue
            m[val] = i
            i += 1
        def val(i: int) -> int:
            return m.get(i, 1001 + i)
        arr1.sort(key=val)
        return arr1