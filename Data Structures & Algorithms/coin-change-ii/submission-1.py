"""
0 -

  use i
  not use i
"""
from functools import lru_cache
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        coins.sort()
        @lru_cache
        def dfs(pos, curr):
            if curr == 0:
                return 1
            if pos >= len(coins):
                return 0
            res = 0
            if curr >= coins[pos]:
                res = dfs(pos+1, curr)
                res += dfs(pos, curr-coins[pos])
            return res
        return dfs(0, amount)