"""
0 -

  use i
  not use i
"""
from functools import lru_cache
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        coins.sort()
        memo = {}
        def dfs(pos, curr):
            if curr == 0:
                return 1
            if pos >= len(coins):
                return 0
            if (pos,curr) in memo:
                return memo[(pos,curr)]
            res = 0
            if curr >= coins[pos]:
                res = dfs(pos+1, curr)
                res += dfs(pos, curr-coins[pos])
                memo[(pos, curr)] = res
            return res
        return dfs(0, amount)