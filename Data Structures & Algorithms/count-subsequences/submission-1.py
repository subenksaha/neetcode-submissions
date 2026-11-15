"""
  c a a a t
c 1 0 0 0 0
a 0 1 2 3 0
t 0 0 0 0 1

"""

class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        if len(t) > len(s):
            return 0
        memo = {}
        def dfs(i, j):
            if j == len(t):
                return 1
            if i == len(s):
                return 0
            key = (i,j)
            if key in memo:
                return memo[key]
            res = dfs(i+1, j)
            if s[i] == t[j]:
                res += dfs(i+1, j+1)
            memo[key] = res
            return res
    
        return dfs(0, 0)
        