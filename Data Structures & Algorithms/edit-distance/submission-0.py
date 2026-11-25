"""
i -- word1
j -- word2

if i == j : dfs(i+1, j+1)
else: 
    insert(i+1, j)
    delete(i-1,j)

"""


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        def dfs(i, j):
            if i == m:
                return n-j
            if j == n:
                return m-i
            if word1[i] == word2[j]:
                return dfs(i+1, j+1)
            else:
                return 1 + min(dfs(i+1, j), dfs(i, j+1), dfs(i+1, j+1))
        return dfs(0, 0)