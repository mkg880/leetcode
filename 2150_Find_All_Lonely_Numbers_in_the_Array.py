class Solution:
    def findLonely(self, nums: List[int]) -> List[int]:
        cnt = Counter(nums)
        res = []
        for key in cnt:
            if cnt[key] == 1 and key+1 not in cnt and key-1 not in cnt:
                res.append(key)
        return res