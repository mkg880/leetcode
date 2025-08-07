import re
class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        raw_words = set(wordlist)
        lowers = {}
        vowels = {}
        for word in wordlist:
            s = word.lower()
            lowers[s] = lowers.get(s, word)
            s = re.sub(r'[aeiou]', '_', s)
            vowels[s] = vowels.get(s, word)
        res = []
        for q in queries:
            add = None
            if q in raw_words:
                add = q
            else:
                s = q.lower()
                if s in lowers:
                    add = lowers[s]
                else:
                    s = re.sub(r'[aeiou]', '_', s)
                    add = vowels.get(s, '')
            res.append(add)
        return res