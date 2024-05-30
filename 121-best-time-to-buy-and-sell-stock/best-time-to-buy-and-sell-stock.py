class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxprofit=0
        buy=float('inf')
        for i in range(0,len(prices)):
            if prices[i]<buy:
                buy=prices[i]
            maxprofit=max(prices[i]-buy,maxprofit)
        return maxprofit