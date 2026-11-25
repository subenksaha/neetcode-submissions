class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sum_ = 0
        for num in nums:
            if sum_ < 0:
                sum_ = 0
            sum_ += num
            
        return sum_
        