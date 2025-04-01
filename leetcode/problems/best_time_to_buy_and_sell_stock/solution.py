class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l=[]
        profit=0
        m=max(prices)+1
        for i in range(len(prices)):
            m=min(m,prices[i])
            profit=max(profit,prices[i]-m)
        return profit

