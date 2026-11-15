class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}
        res = []
        def recursion(amount):
            if amount == 0:
                return 0
            if amount in memo:
                return memo[amount]
            if amount < 0:
                return float("inf")
            
            min_ = float("inf")
            for coin in coins:
                target = amount - coin
                # print(amount, "-", coin, "=", target, count+1)
                min_ = min(min_, 1 + recursion(target))
            memo[amount] = min_
            return min_

        result = recursion(amount)
        return result if result != float("inf") else -1
        