class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False for i in range(len(s) + 1)]
        dp[0] = True
        for i in range(1, len(s) + 1):
            for w in wordDict:
                l = i - len(w)
                if l >= 0 and dp[l] and s[l:i] == w:
                    dp[i] = True
                    break
        return dp[len(s)]