class Solution:
    def findMin(self, nums: List[int]) -> int:
        b = nums[0]
        for i in range(1, len(nums)):
            if nums[i-1] > nums[i]:
                b = nums[i]
        return b