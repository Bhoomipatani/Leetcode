class Solution:
    def canFinish(self, numCourses, prerequisites):
        indegree = [0] * numCourses
        adj = [[] for _ in range(numCourses)]

        for pre in prerequisites:
            adj[pre[1]].append(pre[0])
            indegree[pre[0]]+=1
            # print(indegree,adj)
        q=deque()
        for i in range(numCourses):
            if indegree[i]==0:
                q.append(i)

        visited=0
        while q:
            node=q.popleft()
            visited+=1
            for nei in adj[node]:
                indegree[nei]-=1
                if indegree[nei]==0:
                    q.append(nei)
        # print(visited)
        return visited==numCourses

