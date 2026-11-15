class Solution:
    def __init__(self):
        self.cache = dict()
    def climbStairs(self, n: int) -> int:
        if n < 3: return n
        if n in self.cache: return self.cache[n]
        step = self.climbStairs(n-1) + self.climbStairs(n-2)
        self.cache[n] = step
        return step
        