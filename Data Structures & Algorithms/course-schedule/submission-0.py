class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj_list = dict()

        for (a,b) in prerequisites:
            prev = adj_list.get(b, [])
            prev.append(a)
            adj_list[b] = prev

        visited = set()
        def dfs(node):
            if node in visited: return False
            visited.add(node)
            for dep in adj_list.get(node, []):
                dfs(dep) 

        for node in adj_list:
            if dfs(node) == False:
                return False

        return True