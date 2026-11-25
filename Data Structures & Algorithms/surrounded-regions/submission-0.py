class Solution:
    def solve(self, board: List[List[str]]) -> None:
        dq = deque()
        visited = set()
        m, n = len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                if i == 0 or i == m-1 or j == 0 or j == n-1:
                    if board[i][j] == 'O':
                        dq.append((i,j))
                        visited.add((i,j))

        dirs = [(0,1), (0,-1), (1,0), (-1,0)]
        while dq:
            x, y = dq.popleft()

            for dx, dy in dirs:
                nx, ny = x+dx, y+dy
                if nx < 0 or nx >= m or ny < 0 or ny >= n or (nx, ny) in visited or board[nx][ny] != 'O':
                    continue
                dq.append((nx,ny))
                visited.add((nx,ny))
        for i in range(m):
            for j in range(n):
                if (i,j) not in visited:
                    board[i][j] = 'X'