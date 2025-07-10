class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        if len(arr) <= k:
            return max(arr)
        winner = arr[0]
        rounds = 0
        for num in arr[1:]:
            if winner > num:
                rounds += 1
            else:
                winner = num
                rounds = 1
            if rounds == k:
                return winner
        return winner