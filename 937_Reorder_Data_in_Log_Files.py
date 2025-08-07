class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        def cmp(x, y):
            idx1, idx2 = x.find(' '), y.find(' ')
            a, b = x[idx1+1:], y[idx2+1:]
            if a == b:
                return -1 if x[:idx1] < y[:idx2] else 1
            return -1 if a < b else 1
        
        letters = []
        digits = []
        for s in logs:
            last = s[-1]
            if last.isdigit():
                digits.append(s)
            else:
                letters.append(s)
        letters.sort(key=cmp_to_key(cmp))
        return letters + digits