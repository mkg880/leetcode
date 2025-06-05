class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        m = {0: []}
        dp = [False for i in range(len(s) + 1)]
        dp[0] = True
        for i in range(1, len(s) + 1):
            for w in wordDict:
                l = i - len(w)
                if l >= 0 and dp[l] and s[l:i] == w:
                    dp[i] = True
                    if i not in m:
                        m[i] = []
                    if not m[l]:
                        m[i].append(w)
                    else:
                        for sent in m[l]:
                            m[i].append(sent + " " + w)
        print(m)
        return m.get(len(s), [])