from heapq import heappush, heappop
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        for stone in stones:
            heappush(heap, -stone)

        while len(heap) > 1:
            x = -heappop(heap)
            y = -heappop(heap)
            y = abs(x-y)
            heappush(heap, -y)

        return 0 if not heap else -heap[0]      