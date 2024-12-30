class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i=0
        buy=inf 
        sell=-inf
        profit=0
        while i < len(prices):
            if buy>prices[i]:
                buy=prices[i]
            elif buy<prices[i]:
                sell=prices[i]
            if buy!=inf and sell!=-inf:
                profit+=sell-buy
                buy=inf 
                sell=-inf
            else:
                i+=1
            
        return profit

            