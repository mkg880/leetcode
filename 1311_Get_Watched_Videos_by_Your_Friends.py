class Solution:
    def watchedVideosByFriends(self, watchedVideos: List[List[str]], friends: List[List[int]], id: int, level: int) -> List[str]:
        queue = deque([(id, 0)])
        visited = set()
        friendsLevel = []
        while queue:
            x, d = queue.popleft()
            if x in visited:
                continue
            visited.add(x)
            if d == level:
                friendsLevel.append(x)
            for neighbor in friends[x]:
                queue.append((neighbor, d+1))
        m = {}
        for f in friendsLevel:
            for v in watchedVideos[f]:
                m[v] = m.get(v, 0) + 1
        arr = sorted([(m[key], key) for key in m])
        return [val for _, val in arr]