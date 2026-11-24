class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        minlen = float('inf')

        running = 0
        l = 0
        for r in range(len(nums)):
            running += nums[r]
            while running >= target:
                minlen = min(minlen, r-l+1)
                running -= nums[l]
                l += 1
        return minlen if minlen != float("inf") else 0