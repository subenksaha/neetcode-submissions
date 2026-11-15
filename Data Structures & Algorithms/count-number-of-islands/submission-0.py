class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        dirs = [(1,0),(0,1),(-1,0),(0,-1)]
        def explore(i, j):
            if i < 0 or j < 0 or i >= ROWS or j >= COLS or grid[i][j] == "0":
                return
            grid[i][j] = "0"
            
            for (dx,dy) in dirs:
                nx, ny = i+dx, j+dy
                explore(nx, ny)
        count = 0
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == "1" :
                    explore(i, j)
                    count += 1
        return count

        