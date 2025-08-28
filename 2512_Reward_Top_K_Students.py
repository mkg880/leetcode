import heapq
class Solution:
    def topStudents(self, positive_feedback: List[str], negative_feedback: List[str], report: List[str], student_id: List[int], k: int) -> List[int]:
        heap = []
        pos, neg = set(positive_feedback), set(negative_feedback)
        for id, r in zip(student_id, report):
            score = 0
            for word in r.split():
                if word in pos:
                    score += 3
                if word in neg:
                    score -= 1
            curr = (score, -id)
            if len(heap) == k and curr > heap[0]:
                heapq.heappop(heap)
            if len(heap) < k:
                heapq.heappush(heap, curr)
        res = []
        while heap:
            _, id = heapq.heappop(heap)
            res.append(-id)
        return list(reversed(res))