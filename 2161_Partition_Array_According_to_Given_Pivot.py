class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        cnt = 0
        l, r = [], []
        for val in nums:
            if val < pivot:
                l.append(val)
            elif val > pivot:
                r.append(val)
            else:
                cnt += 1
        return l + [pivot] * cnt + r