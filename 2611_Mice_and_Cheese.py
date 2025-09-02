class Solution:
    def miceAndCheese(self, reward1: List[int], reward2: List[int], k: int) -> int:
        res = 0
        arr = [i for i in range(len(reward1))]
        def cmp(i):
            return reward1[i] - reward2[i]
        arr.sort(reverse=True, key=cmp)
        for i in range(len(arr)):
            if i < k:
                res += reward1[arr[i]]
            else:
                res += reward2[arr[i]]
        return res