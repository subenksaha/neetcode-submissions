class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj_list = dict()

        for (a,b) in prerequisites:
            prev = adj_list.get(a, [])
            prev.append(b)
            adj_list[a] = prev

        visiting = set()
        def dfs(node):
            if node in visiting:
                return False
            if adj_list.get(node, []) == []:
                return True

            visiting.add(node)
            for pre in adj_list.get(node, []):
                if not dfs(pre):
                    return False
            visiting.remove(node)
            adj_list[node] = []
            return True

        for node in adj_list:
            if dfs(node) == False:
                return False

        return True