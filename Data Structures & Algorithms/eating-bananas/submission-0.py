class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def eatWithinK(k):
            count = 0
            for pile in piles:
                count += math.ceil(pile / k)

            return count <= h
    
        low, high = 1, max(piles)

        while low < high:
            mid = (low+high) // 2
            if eatWithinK(mid):
                high = mid
            else:
                low = mid+1
        return low
        