class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        m, n = len(grid), len(grid[0])
        dq = deque()

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    dq.append((i,j,0))

        dirs = [(1,0), (-1,0), (0,1), (0,-1)]
        visited = set()
        while dq:
            x, y, d = dq.popleft()
            if grid[x][y] > d:
                grid[x][y] = d
            for dx, dy in dirs:
                nx, ny = x+dx, y+dy
                if nx < 0 or nx >= m or ny < 0 or ny >= n or (nx,ny) in visited or grid[nx][ny] == -1:
                    continue
                dq.append((nx,ny, d+1))
                visited.add((nx,ny))

        
        