from heapq import heappush, heappop
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        maxheap = []
        for num in arr:
            heappush(maxheap, (-abs(num-x), -num))
            if len(maxheap) > k:
                heappop(maxheap)
        
        res = []
        for item in maxheap:
            res.append(-item[1])
        return sorted(res)