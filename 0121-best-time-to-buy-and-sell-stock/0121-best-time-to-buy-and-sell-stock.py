class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        
        l = 0
        n = len(prices)
        r = 1
        
        while r<n:
            
            
            if prices[r] > prices[l]:
                cur_profit = prices[r]-prices[l] 
                max_profit = max(max_profit, cur_profit)
            
            else:
                l = r
            r += 1
        
        return max_profit
    
    # time complexity = O(N)
    