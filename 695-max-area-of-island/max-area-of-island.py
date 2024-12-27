class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def bfs(i,j,visitedarr,grid):
            area=0
            nonlocal maxarea
            q=deque([(i,j)])
            while q:
                i,j=q.popleft()
                if 0<=i<len(grid) and 0<=j<len(grid[0]) and grid[i][j]==1 and visitedarr[i][j]==0:
                    visitedarr[i][j]=1
                    area+=1
                    q.extend([(i-1,j),(i+1,j),(i,j-1),(i,j+1)])
                    
            maxarea=max(maxarea,area)

        maxarea=0
        m=len(grid[0])
        n=len(grid)
        visitedarr=[[0]*m for i in range(n)]
        for i in range(n):
            for j in range(m):
                if visitedarr[i][j]==0 and grid[i][j]==1:
                    bfs(i,j,visitedarr,grid)
        return maxarea