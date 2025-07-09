class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        start = 0
        curr = s[0]
        arr = []
        for end in range(len(s)):
            if s[end] == curr:
                end += 1
            else:
                val = (end - start) % k
                if val:
                    if arr and curr == arr[-1][0]:
                        val += arr[-1][1]
                        val = val % k
                        if val:
                            arr[-1][1] = val
                        else:
                            arr.pop()
                    else:
                        arr.append([curr, val])
                start = end
                curr = s[end]
        val = (len(s) - start) % k
        if val:
            if arr and curr == arr[-1][0]:
                val += arr[-1][1]
                val = val % k
                if val:
                    arr[-1][1] = val
                else:
                    arr.pop()
            else:
                arr.append([curr, val])
        return "".join([a * b for a, b in arr])