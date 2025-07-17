class FindSumPairs:

    def __init__(self, nums1: List[int], nums2: List[int]):
        self.nums1 = nums1
        self.nums2 = nums2
        self.m = {}
        for val in nums2:
            self.m[val] = self.m.get(val, 0) + 1

    def add(self, index: int, val: int) -> None:
        x = self.nums2[index]
        self.m[x] -= 1
        self.m[x + val] = self.m.get(x+val, 0) + 1
        self.nums2[index] += val 

    def count(self, tot: int) -> int:
        res = 0
        for val in self.nums1:
            res += self.m.get(tot - val, 0)
        return res


# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)