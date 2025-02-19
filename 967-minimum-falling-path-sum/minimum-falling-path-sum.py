class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        dp = [[float("inf")]*n for _ in range(n)]

        def helper(i,j,dp):
            if i == len(matrix):
                return 0
            if j < 0 or j >=  n:
                return float("inf")
            if dp[i][j] != float("inf"):
                return dp[i][j]
            pickD = matrix[i][j] + helper(i+1,j,dp)
            pickL = matrix[i][j] + helper(i+1,j-1,dp)
            pickR = matrix[i][j] + helper(i +1 ,j+1,dp)
            dp[i][j] = min(pickD , pickL,pickR)
            return dp[i][j]

        ans = float("inf")
        for j in range(len(matrix[0])):
            ans = min(ans,helper(0,j,dp))
        return ans