class Solution:
    def countSubstrings(self, s: str) -> int:
        q = deque()
        cnt = 0
        for i in range(len(s)):
            q.append([i, i])
            cnt += 1
            if i + 1 < len(s) and s[i+1] == s[i]:
                q.append([i, i+1])
                cnt += 1
        while q:
            i, j = q.popleft()
            if i-1 >= 0 and j+1 < len(s) and s[i-1] == s[j+1]:
                q.append([i-1, j+1])
                cnt += 1
        return cnt