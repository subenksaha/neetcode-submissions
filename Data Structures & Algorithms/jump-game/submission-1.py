class Solution:
    def canJump(self, nums: List[int]) -> bool:
        jump = 0
        for i, num in enumerate(nums):
            if i == jump:
                jump += num
        return jump >= len(nums) - 1