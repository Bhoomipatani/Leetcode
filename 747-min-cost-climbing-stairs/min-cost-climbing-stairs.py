class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp = [-1] * n
        def dfs(i):
            if dp[i] != -1:
                return dp[i]
            if i <= 1:
                dp[i] = cost[i]
            else:
                dp[i] = cost[i] + min(dfs(i-1), dfs(i-2))
            return dp[i]
        return min(dfs(n-1), dfs(n-2))