"""
Day 1 
  - hold
    - sell
    - hold
  - not hold
    - buy
    - hold
"""
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo = {}
        def subproblem(day, holding):
            if day >= len(prices):
                return 0
            if (day, holding) in memo:
                return memo[(day, holding)]
            if holding:
                memo[(day, holding)] = max(subproblem(day+1, True), prices[day] + subproblem(day+2, False))
                return memo[(day, holding)]
            else:
                memo[(day, holding)] = max(subproblem(day+1, False), subproblem(day+1, True) - prices[day])
                return memo[(day, holding)]

        return subproblem(0, False)