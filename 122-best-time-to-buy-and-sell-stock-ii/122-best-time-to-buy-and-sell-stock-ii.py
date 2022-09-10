class Solution:
    def maxProfit(self, prices: List[int]) -> int:
#         valley = prices[0]
#         peak = prices[0]
#         profit = 0
#         i = 0
#         while i < len(prices)-1:
#             while i+1 < len(prices) and prices[i] >= prices[i+1]:
#                 i += 1
#             valley = prices[i]
#             while i+1< len(prices) and prices[i] <= prices[i+1]:
#                 i+= 1
#             peak = prices[i]
            
#             profit += peak-valley
#         return profit
                
        profit = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                profit += prices[i]-prices[i-1]
        return profit