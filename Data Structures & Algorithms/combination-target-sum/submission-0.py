class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, arr, ttl):
            if i >= len(nums) or ttl > target: return
            if ttl == target:
                res.append(arr[:])
                return
            arr.append(nums[i])
            dfs(i, arr, ttl + nums[i])
            arr.pop()
            dfs(i+1, arr, ttl)
        
        dfs(0, [], 0)

        return res