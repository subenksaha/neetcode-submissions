class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        count = 0
        for num in nums:
            count |= 1 << num
        n = nums[-1]
        m = 0
        for i in range(n):
            if count & (1 << i):
                continue
            m = i

        return m