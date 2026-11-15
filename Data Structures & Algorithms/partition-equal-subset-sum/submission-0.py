"""
n = length
1,2,3,4,5
left_sum, i, right sum

"""
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        ttl = sum(nums)
        if ttl % 2: return False
        target = ttl //2
        def partition(ind, target):
            if ind >= len(nums):
                return target == 0
            if target < 0:
                return False
            
            return partition(ind+1, target-nums[ind]) or partition(ind+1, target)
        
        
        return partition(0, target)
        