class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adjList = collections.defaultdict(list)
        indegree = collections.defaultdict(int)

        for src, dst in prerequisites:
            adjList[src].append(dst)
            indegree[dst] += 1
        
        dq = deque()
        res = []
        for node in range(numCourses):
            if indegree[node] == 0:
                dq.append(node)
        finished = 0
        while dq:
            curr = dq.popleft()
            res.append(curr)
            finished += 1
            for nei in adjList[curr]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    dq.append(nei)
        if finished != numCourses:
            return []
        return res[::-1]