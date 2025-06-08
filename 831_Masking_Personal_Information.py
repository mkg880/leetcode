class Solution:
    def maskPII(self, s: str) -> str:
        if not s[0].isalpha():
            digits = ''.join(filter(str.isdigit, s))
            country = len(digits) - 10
            if country == 0:
                return '***-***-' + digits[-4:]
            else:
                return '+' + '*'*country + '-***-***-' + digits[-4:]
        else:
            name, domain = s.split('@')
            return (name[0] + '*****' + name[-1] + '@' + domain).lower()