class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        m = {}
        res = 0
        for word in words:
            rev = word[1] + word[0]
            if rev in m and m[rev] > 0:
                res += 4
                m[rev] -= 1
            else:
                m[word] = m.get(word, 0) + 1
        for key in m:
            if m[key] > 0 and key[0] == key[1]:
                res += 2
                return res
        return res