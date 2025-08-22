class Solution:
    def countDistinct(self, nums: List[int], k: int, p: int) -> int:
        n = len(nums)
        res = set()
        for i in range(n):
            cnt = 0
            curr = []
            for j in range(i, n):
                if nums[j] % p == 0:
                    cnt += 1
                if cnt > k:
                    break
                curr.append(nums[j])
                res.add(tuple(curr))
        return len(res)