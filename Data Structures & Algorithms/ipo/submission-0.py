from heapq import heappush, heappop
class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        profitQ = []
        capitalQ = []
        for profit, expand in zip(profits, capital):
            heappush(capitalQ, (expand, -profit))

        while capitalQ or profitQ:
            while capitalQ and capitalQ[0][0] <= w:
                capital, profit = heappop(capitalQ)
                heappush(profitQ, (profit, capital))
            if profitQ:
                profit, capital = heappop(profitQ)
                w += -profit
                k -= 1
                if k <= 0:
                    break
        return w