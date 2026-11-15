from collections import defaultdict
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numDict = defaultdict(int)
        length = 0

        for num in nums:
            if not numDict[num]:
                numDict[num] = numDict[num-1] + numDict[num+1] + 1
                numDict[num - numDict[num-1]] = numDict[num]
                numDict[num + numDict[num+1]] = numDict[num]
                length = max(length, numDict[num])
        return length

        