class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        v4 = '.' in queryIP
        v6 = ':' in queryIP
        if v4 == v6:
            return "Neither"
        if v4:
            arr = queryIP.split(".")
            if len(arr) != 4:
                return "Neither"
            for s in arr:
                if not s.isdigit() or not 0 <= int(s) <= 255 or (len(s) > 1 and s[0] == '0'):
                    return "Neither"
            return "IPv4"
        arr = queryIP.split(':')
        if len(arr) != 8:
            return "Neither"
        for s in arr:
            if len(s) < 1 or len(s) > 4:
                return "Neither"
            for c in s:
                if c.isalpha() and c.lower() > 'f':
                    return "Neither"
        return "IPv6"