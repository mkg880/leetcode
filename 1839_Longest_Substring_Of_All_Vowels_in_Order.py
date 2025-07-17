class Solution:
    def longestBeautifulSubstring(self, word: str) -> int:
        start = word.find('a')
        end = start
        res = 0
        order = ['a', 'e', 'i', 'o', 'u']
        valid = True
        while start != -1:
            valid = True
            for c in order:
                prev = end
                while end < len(word) and word[end] == c:
                    end += 1
                if end == prev:
                    valid = False
                    break
            if valid:
                res = max(res, end - start)
            start = word.find('a', end)
            end = start
        return res