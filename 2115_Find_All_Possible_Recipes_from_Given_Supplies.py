from collections import deque
class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        res = []
        graph = {}
        indeg = {}
        n = len(recipes)
        for i in range(n):
            for ingredient in ingredients[i]:
                if ingredient not in graph:
                    graph[ingredient] = []
                graph[ingredient].append(recipes[i])
                indeg[recipes[i]] = indeg.get(recipes[i], 0) + 1
        q = deque(supplies)
        while q:
            curr = q.popleft()
            for neighbor in graph.get(curr, []):
                indeg[neighbor] = indeg.get(neighbor, 1) - 1
                if indeg[neighbor] == 0:
                    q.append(neighbor)
                    res.append(neighbor)
            graph[curr] = []
        return res