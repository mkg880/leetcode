class Solution:
    def expressiveWords(self, s: str, words: List[str]) -> int:
        def get_groups(st):
            curr = st[0]
            i = 1
            cnt = 1
            arr = []
            while i < len(st):
                if st[i] == curr:
                    cnt += 1
                else:
                    arr.append((curr, cnt))
                    cnt = 1
                    curr = st[i]
                i += 1
            arr.append((curr, cnt))
            return arr
        target = get_groups(s)
        res = 0
        for word in words:
            arr = get_groups(word)
            if len(arr) != len(target):
                continue
            valid = True
            for (c1, cnt1), (c2, cnt2) in zip(arr, target):
                if c1 != c2 or (cnt1 != cnt2 and (cnt1 > cnt2 or cnt2 < 3)):
                    valid = False
                    break
            if valid:
                res += 1
        return res