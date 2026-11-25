class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        visited = set()
        perimeter = 0
        def dfs(x,y):
            nonlocal perimeter
            if x < 0 or x >= m or y < 0 or y >= n or (x,y) in visited:
                return

            if grid[x][y] == 1:
                if x-1 < 0 or grid[x-1][y] != 1:
                    perimeter += 1
                if x+1 >= m or grid[x+1][y] != 1:
                    perimeter += 1
                if y-1 < 0 or grid[x][y-1] != 1:
                    perimeter += 1
                if y+1 >= n or grid[x][y+1] != 1:
                    perimeter += 1
            visited.add((x,y))
            dfs(x+1, y)
            dfs(x-1, y)
            dfs(x, y+1)
            dfs(x, y-1)
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    dfs(i, j)
                    break

        return perimeter