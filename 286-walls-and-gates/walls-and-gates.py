class Solution:
    def wallsAndGates(self, grid: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        if not grid or not grid[0]:
            return

        m = len(grid[0])
        n = len(grid)
        infi = (2**31) - 1

        q = deque()
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0:
                    q.append((i, j))

        while q:
            x, y = q.popleft()
            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] == infi:
                    grid[nx][ny] = grid[x][y] + 1
                    q.append((nx, ny))

