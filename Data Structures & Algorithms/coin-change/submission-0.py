class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = { 0 : 0 }
        res = []
        def recursion(amount, count):
            if amount == 0:
                return count
            if amount < 0:
                return float("inf")
            
            min_ = float("inf")
            for coin in coins:
                target = amount - coin
                # print(amount, "-", coin, "=", target, count+1)
                min_ = min(min_, recursion(target, count + 1))

            return min_

        result = recursion(amount, 0)
        return result if result != float("inf") else -1
        