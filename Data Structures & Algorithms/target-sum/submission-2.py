"""
target
    target - pos, pos+1
    target + pos,  pos +1
"""

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {}
        def dfs(pos, curr):
            if pos == len(nums):
                return target == curr
            if (pos, curr) in memo:
                return memo[(pos,curr)]
            res = dfs(pos+1, curr + nums[pos]) + dfs(pos+1, curr - nums[pos])
            memo[(pos,curr)] = res
            return res

        return dfs(0, 0)
        