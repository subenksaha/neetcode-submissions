from collections import defaultdict
class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adj = defaultdict(list)
        for u,v in prerequisites:
            adj[v].append(u)
        
        prereqMap = {}
        def dfs(crs):
            if crs not in prereqMap:
                prereqMap[crs] = set()
                for prepreq in adj[crs]:
                    prereqMap[crs] |= dfs(prepreq)
                prereqMap[crs].add(crs)
            return prereqMap[crs]
        for crs in range(numCourses):
            dfs(crs)
        res = []
        for u, v in queries:
            res.append(u in prereqMap[v])
        return res