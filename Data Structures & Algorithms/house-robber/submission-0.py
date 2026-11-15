class Solution:
    def __init__(self):
        self.cache = {}
    def rob(self, nums: List[int]) -> int:
        def dfs(i):
            if i > len(nums)-1: return 0
            if i in self.cache: return self.cache[i]
            max_ = max(nums[i] + dfs(i+2), dfs(i+1))
            self.cache[i] = max_
            return max_
        return dfs(0)
        