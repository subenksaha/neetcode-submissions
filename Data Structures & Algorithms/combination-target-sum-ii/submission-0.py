class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []

        def dfs(pos, subset, ttl):
            if ttl == target:
                res.append(subset[:])
                return
            if ttl > target or pos == len(candidates):
                return
            
            subset.append(candidates[pos])
            dfs(pos+1, subset, ttl + candidates[pos])
            subset.pop()

            while pos + 1 < len(candidates) and candidates[pos] == candidates[pos+1]:
                pos += 1

            dfs(pos+1, subset, ttl)
        dfs(0, [], 0)

        return res