"""
target
    target - pos, pos+1
    target + pos,  pos +1
"""

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {}
        def dfs(pos, curr):
            if pos >= len(nums):
                return 0
            if target == curr:
                return 1
            if (pos, curr) in memo:
                return memo[(pos,curr)]
            res = 0
            res = dfs(pos+1, curr + nums[pos])
            res += dfs(pos+1, curr - nums[pos])
            memo[(pos,curr)] = res
            return pos

        return dfs(0, 0)
        