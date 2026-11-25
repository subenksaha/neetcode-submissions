#   c r a b t
# c 1 1 1 1 1
# a 0 0 2 2 2
# t 0 0 0 0 3


#   a b c d
# a 1 0 0 0
# b 0 2 0
# c 0 0 3
# d 0 0 0 4
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        dp = [ [-1] * len(text2) for _ in range(len(text1)) ]
        # print(dp)
        def dfs(i, j):
            if i < 0 or j < 0:
                return 0
            if dp[i][j] != -1:
                return dp[i][j]
            if text1[i] == text2[j]:
                dp[i][j] = 1 + max(dfs(i-1, j), dfs(i, j-1))
            else:
                dp[i][j] = max(dfs(i-1, j), dfs(i, j-1))
            return dp[i][j]
        # print(dp)
        return dfs(m-1, n-1)
