class Solution:
    def maxTaxiEarnings(self, n: int, rides: List[List[int]]) -> int:
        dp=[0]*(n+1)
        max_profit=0
        point=defaultdict(list)
        for start,end,tip in rides:
            point[start].append((end,end-start+tip))

        for i in range(1,n+1):
            max_profit=max(max_profit, dp[i])
            dp[i]=max_profit
            for end, profit in point[i]:
                dp[end] = max(dp[end], dp[i] + profit)
        
        return max(dp)