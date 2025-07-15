class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        heap = []
        for i in range(len(classes)):
            a, b = classes[i]
            change = ((a+1) / (b+1)) - (a/b)
            heappush(heap, (-change, i))
        for i in range(extraStudents):
            _, i = heappop(heap)
            classes[i][0] += 1
            classes[i][1] += 1
            a, b = classes[i]
            change = ((a+1) / (b+1)) - (a/b)
            heappush(heap, (-change, i))
        total = 0
        for a, b in classes:
            total += a / b
        return total / len(classes)