class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visitedarr=[[0]*len(grid[0]) for _ in range(len(grid))]
        n=len(grid)
        m=len(grid[0])
        island=0
        def bfs(i,j,visitedarr,grid):
            q=deque([(i,j)])
            while q:
                i,j=q.popleft()
                if 0<=i<len(grid) and 0<=j<len(grid[0]) and grid[i][j]=='1'and visitedarr[i][j]==0:
                    visitedarr[i][j]=1
                    q.extend([(i-1,j),(i+1,j),(i,j-1),(i,j+1)])
        for i in range(n):
            for j in range(m):
                if visitedarr[i][j]==0 and grid[i][j]=='1':
                    island+=1
                    bfs(i,j,visitedarr,grid)
                    
        return island
        
