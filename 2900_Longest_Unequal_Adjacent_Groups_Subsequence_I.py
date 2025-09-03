class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        res = [words[0]]
        curr = groups[0]
        for i in range(1, len(words)):
            if groups[i] != curr:
                curr = groups[i]
                res.append(words[i])
        return res