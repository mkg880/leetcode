class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        a, b = 0, 0
        for i in range(len(s)):
            if s[i] in vowels:
                if i < len(s) / 2:
                    a += 1
                else:
                    b += 1
        return a == b