class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adjList = [[] for i in range(numCourses)]
        indeg = {i: 0 for i in range(numCourses)}
        for a, b in prerequisites:
            adjList[b].append(a)
            indeg[a] += 1
        res = []
        while len(res) < numCourses:
            choice = None
            for node in indeg:
                if indeg[node] == 0:
                    choice = node
                    break
            if choice == None:
                return []
            for neighbor in adjList[choice]:
                indeg[neighbor] -= 1
            adjList[choice] = []
            del indeg[choice]
            res.append(choice)
        return res