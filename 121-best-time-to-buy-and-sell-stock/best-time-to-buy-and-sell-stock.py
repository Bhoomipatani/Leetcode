class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxdiff=0
        minprice=prices[0]
        for i in range(1,len(prices)):
            minprice=min(prices[i],minprice)
            maxdiff=max(maxdiff,prices[i]-minprice)
        return maxdiff