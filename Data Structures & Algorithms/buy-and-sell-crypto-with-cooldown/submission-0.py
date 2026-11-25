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
        def subproblem(day, holding):
            if day >= len(prices):
                return 0
            if holding:
                return max(subproblem(day+1, True), prices[day] + subproblem(day+2, False))
            else:
                return max(subproblem(day+1, False), subproblem(day+1, True) - prices[day])

        return subproblem(0, False)