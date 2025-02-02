class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        n=len(matrix)
        m=len(matrix[0])
        dp=[[0]*(m+1) for j in range(n+1)]
        ans=0
        
        for i in range(1,len(dp)):
            for j in range(1,len(dp[0])):
                # print(i,j)
                if matrix[i-1][j-1]!='0' :
                    dp[i][j]=min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1])+1
                    ans=max(ans,dp[i][j]*dp[i][j])
            # print(dp)
            
        return ans