class Solution:
    def mincostTickets(self, days: List[int], cost: List[int]) -> int:
        dp=[0]*366
        for i in range(1,len(dp)):
            if i not in days:
                dp[i]=dp[i-1]
            else:
                cost1=dp[i-1]+cost[0]
                cost7=dp[max(0,i-7)]+cost[1]
                cost30=dp[max(0,i-30)]+cost[2]
                dp[i]=min(cost1,cost7,cost30)
        return dp[365]