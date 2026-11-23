class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i, k, n = 0, 0, len(nums)

        while k < n:
            nums[i] = nums[k]
            while k < n and nums[i] == nums[k]:
                k += 1
            i += 1
            
        return i