from typing import Counter, List
class Solution:
    def reportSpam(self, message: List[str], bannedWords: List[str]) -> bool:
        c = Counter(message)
        return sum(c.get(word, 0) for word in set(bannedWords)) >= 2