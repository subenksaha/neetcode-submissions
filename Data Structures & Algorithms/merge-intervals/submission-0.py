class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        result = [intervals[0]]

        slow, fast = 0 ,1

        # [1, 3] - [2, 4]
        # [1, 6] - [2, 4]
        while fast < len(intervals):
            curr = result[slow]
            next_ = intervals[fast]
            if curr[0] <= next_[0] <= curr[1]:
                curr[1] = max(curr[1], next_[1])
                fast += 1
            else:
                result.append(intervals[fast])
                fast += 1
                slow += 1
        return result

        