"""
0 ->
  i + 1 -> 1
    - 2
    - 3
  i + 2
1 ->
  i + 1
  i + 2

"""
from functools import lru_cache
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        @lru_cache
        def dp(start):
            if start >= len(cost):
                return 0
            return min(cost[start] + dp(start+1), cost[start] + dp(start+2))
        
        return min(dp(0), dp(1))

        