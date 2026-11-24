class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        max_cap = sum(weights)
        min_cap = max(weights)

        def isPossible(cap):
            count  = 1
            running = 0
            for weight in weights:
                if running + weight <= cap:
                    running += weight
                else:
                    running = weight
                    count += 1
            return count <= days

        while min_cap < max_cap:
            cap = (max_cap + min_cap) // 2
            if isPossible(cap):
                max_cap = cap
            else:
                min_cap = cap+1

        return min_cap
        