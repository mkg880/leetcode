class Solution:
    def countVowels(self, word: str) -> int:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        n = len(word)
        res = 0
        for i in range(n):
            if word[i] in vowels:
                res += (i+1) * (n-i)
        return res