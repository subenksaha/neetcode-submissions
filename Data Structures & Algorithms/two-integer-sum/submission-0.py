class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        gaps = dict()
        for i, num in enumerate(nums):
            if num in gaps:
                return sorted([i, gaps.get(num)]) 
            gap = target - num
            gaps[gap] = i
        
        