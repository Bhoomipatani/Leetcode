class Solution:
    def numSquares(self, n: int) -> int:
        arr=[]
        for i in range(1,n+1):
            if i*i>n:
                break
            arr.append(i*i)
        dp=[float('inf')]*(n+1)
        dp[0]=0
        for i in range(1,n+1):
            for square in arr:
                if i<square:
                    break
                dp[i]=min(dp[i],dp[i-square]+1)
        return dp[-1]