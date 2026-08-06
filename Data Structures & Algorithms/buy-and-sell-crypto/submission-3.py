class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i = 1
        buy = 0
        max_profit = 0

        while i < len(prices):
            max_profit = max(max_profit, prices[i]-prices[buy])
            if prices[i] < prices[buy]:
                buy = i
            i+=1
        return max_profit
        