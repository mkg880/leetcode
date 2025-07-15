class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        heap = []
        for i in range(1, len(heights)):
            if heights[i] <= heights[i-1]:
                continue
            diff = heights[i] - heights[i-1]
            if len(heap) < ladders:
                heappush(heap, diff)
            elif heap and diff > heap[0]:
                popped = heappop(heap)
                heappush(heap, diff)
                bricks -= popped
            else:
                bricks -= diff
            if bricks < 0:
                return i-1
        return len(heights) - 1