class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        o = []
        unlocked = []
        n = len(s)
        if n % 2 != 0:
            return False
        for i in range(n):
            if locked[i] == '0':
                unlocked.append(i)
            elif s[i] == '(':
                o.append(i)
            else:
                if o:
                    o.pop()
                elif unlocked:
                    unlocked.pop()
                else:
                    return False
        while o and unlocked and o[-1] < unlocked[-1]:
            o.pop()
            unlocked.pop()
        return not o