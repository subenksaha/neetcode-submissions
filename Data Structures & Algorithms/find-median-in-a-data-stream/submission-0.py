import heapq
class MedianFinder:

    def __init__(self):
        self.left = []
        self.right = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.right, num)
        while len(self.left)+1 < len(self.right):
            curr = heapq.heappop(self.right)
            heapq.heappush(self.left, -curr)

    def findMedian(self) -> float:
        if len(self.left) == len(self.right):
            l = -1 * self.left[0]
            r = self.right[0]
            return (l+r) / 2
        elif len(self.left) < len(self.right):
            return self.right[0]
        else:
            return -1 * self.left[0]
        