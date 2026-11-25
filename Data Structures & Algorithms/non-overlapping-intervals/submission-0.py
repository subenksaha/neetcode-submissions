class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x: ((x[1] - x[0])))
        isOverlap = dict()
        count = 0
        for interval in intervals:
            for i in range(interval[0], interval[1]):
                if i in isOverlap:
                    count += 1
                    break
                isOverlap[i] = True

        return count
        