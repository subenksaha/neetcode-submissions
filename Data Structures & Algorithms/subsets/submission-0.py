class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        def dfs(pos, sub):
            if pos >= len(nums):
                res.append(sub[:])
                return
            if pos > 0 and nums[pos-1] == nums[pos]:
                pos += 1
            sub.append(nums[pos])
            dfs(pos+1, sub)
            sub.pop()
            dfs(pos+1, sub)
        dfs(0, [])
        return res