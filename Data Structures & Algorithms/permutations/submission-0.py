class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        def recursion(permutation):
            if len(permutation) == len(nums):
                result.append(permutation)
                return
            if len(permutation) > len (nums):
                return
            for num in nums:
                if num in permutation:
                    continue
                recursion(permutation + [num])
        recursion([])
        return result