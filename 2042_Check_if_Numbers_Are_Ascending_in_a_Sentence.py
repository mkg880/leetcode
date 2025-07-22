class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        curr = -1
        for token in s.split():
            if token.isdigit():
                val = int(token)
                if val <= curr:
                    return False
                curr = val
        return True