class Solution:
    def maximumNumber(self, num: str, change: List[int]) -> str:
        i = 0
        curr = int(num[0])
        while i < len(num) and curr >= change[curr]:
            i += 1
            if i < len(num):
                curr = int(num[i])
        j = i
        while j < len(num) and curr <= change[curr]:
            j += 1
            if j < len(num):
                curr = int(num[j])
        return num[:i] + ''.join([str(change[int(num[idx])]) for idx in range(i, j)]) + num[j:]