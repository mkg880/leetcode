class Solution:
    def wordCount(self, startWords: List[str], targetWords: List[str]) -> int:
        sorted_start_words = {''.join(sorted(word)) for word in startWords}
        res = 0
        for t in targetWords:
            t = ''.join(sorted(t))
            for i in range(len(t)):
                if t[:i] + t[i+1:] in sorted_start_words:
                    res += 1
                    break
        return res