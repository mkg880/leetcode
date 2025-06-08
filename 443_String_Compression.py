class Solution:
    def compress(self, chars: List[str]) -> int:
        i = 0
        res = 0
        while(i < len(chars)):
            curr = chars[i]
            cnt = 0
            while(i < len(chars) and chars[i] == curr):
                cnt += 1
                i += 1
            chars[res] = curr
            res += 1
            if cnt > 1:
                for c in str(cnt):
                    chars[res] = c
                    res += 1
        return res