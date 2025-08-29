class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        n = len(words)
        pre = [0] * (n+1)
        curr = 0
        vowels = {'a', 'e', 'i', 'o', 'u'}
        for i in range(n+1):
            pre[i] = curr
            if i < n and words[i][0] in vowels and words[i][-1] in vowels: curr += 1
        return [pre[r+1] - pre[l] for l, r in queries]