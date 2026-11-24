from collections import defaultdict
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        tbl = defaultdict(int)
        l = 0
        for r in range(len(nums)):
            if tbl[nums[r]] > 0:
                return True
            tbl[nums[r]] += 1
            if r-l >= k:
                tbl[nums[l]] -= 1
                l += 1
        return False