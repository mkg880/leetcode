class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        m = {}
        for s in cpdomains:
            rep, url = s.split()
            rep = int(rep)
            parts = url.split('.')
            n = len(parts)
            curr = ''
            for i in range(n-1, -1, -1):
                x = parts[i]
                if i < n-1:
                    x += '.'
                curr = x + curr
                m[curr] = m.get(curr, 0) + rep
        return [f"{m[key]} {key}" for key in m]
