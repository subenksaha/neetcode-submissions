from heapq import heappush, heappop

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        heap = []
        result = []
        for i in range(0, len(nums)):
            heappush(heap, (-1 * nums[i], i))
            if i < k-1 : continue
            while not i-k-1 <= heap[0][1]: heappop(heap)
            result.append(-1 * heap[0][0])
        return result