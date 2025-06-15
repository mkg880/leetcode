class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        dp = [0] * (len(books) + 1)
        for i in range(len(books)):
            (width, height) = books[i]
            new_val = dp[i] + height
            for j in range(i, 0, -1):
                width += books[j-1][0]
                if width > shelfWidth:
                    break
                height = max(height, books[j-1][1])
                new_val = min(new_val, dp[j-1] + height)
            dp[i+1] = new_val
        return dp[len(books)]