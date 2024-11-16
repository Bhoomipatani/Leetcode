class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        
        n = len(isConnected)        
        adj = [set() for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if isConnected[i][j] == 1 and i != j:
                    adj[i].add(j)
                    adj[j].add(i)
        
        visited = [False] * n
        
        def dfs(node):
            for neighbor in adj[node]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    dfs(neighbor)
        
        province_count = 0
        for i in range(n):
            if not visited[i]:
                visited[i] = True
                dfs(i)
                province_count += 1
        
        return province_count