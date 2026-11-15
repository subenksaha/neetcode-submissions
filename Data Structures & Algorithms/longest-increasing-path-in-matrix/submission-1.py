"""
[
[1, 2]
[3, 4]
]

[
[0, 1]
[1, 2]
]
"""


class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        rows = len(matrix)
        cols = len(matrix[0])
        memo = {}
        def dfs(i, j, prevValue):
            if i < 0 or j < 0 or i >= rows or j >= cols or matrix[i][j] <= prevValue:
                return 0
            key = (i,j)
            if key in memo:
                return memo[key]
            res = 1
            for (dx, dy) in [(-1,0), (1,0), (0, 1), (0, -1)]:
                nx, ny = i+dx, j+dy
                res = max(res, 1+dfs(nx, ny, matrix[i][j]))
            memo[key] = res
            return res
        LIP = 0
        for i in range(rows):
            for j in range(cols):
                LIP = max(LIP, dfs(i, j, float('-inf')))

        return LIP