class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        s = set(bank)
        if endGene not in s and endGene != startGene:
            return -1
        q = deque()
        q.append((startGene, 0))
        visited = set()
        visited.add(startGene)
        while q:
            word, distance = q.popleft()
            if word == endGene:
                return distance
            for i in range(8):
                for c in 'ACGT':
                    if word[i] != c:
                        new_word = word[:i] + c + word[i+1:]
                        if new_word in s and new_word not in visited:
                            q.append((new_word, distance + 1))
                            visited.add(new_word)
        return -1
